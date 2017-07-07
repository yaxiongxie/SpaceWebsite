# coding: UTF-8

from django.shortcuts import render,HttpResponseRedirect
from PIL import Image, ImageDraw, ImageFont
from django.http.response import HttpResponse
from SpaceWebsite.settings import BASE_DIR
import cStringIO, string, os, random
import json
import uuid
from models import Account
from publish.models import News
from models import ServiceRequirement,OfficeBuildingList,OfficeList,HouseSource,HouseRequirement,Corporation,Order,Messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from commonData.models import SourceType,Subway,Area,District,ServiceType,Services
from django.db.models import Q
import time


def clearSession(request):
    request.session["headSubmit"] = ""
    return HttpResponse("success")

def exit(request):
    del request.session["login"]
    return HttpResponseRedirect(request.GET["returnUrl"])

def addSource(request):
    if request.method == "POST":
        title=request.POST.get("title")
        telephone = request.POST.get("telephone")
        username = request.POST.get("username")
        area_type=request.POST.get("area_type")

        houseSource = HouseSource()
        houseSource.telephone=telephone
        houseSource.username=username
        houseSource.title=title

        houseSource.save()
        request.session["headSubmit"] = "yes"
        return HttpResponseRedirect(request.GET["returnUrl"])


def addRequest(request):
    if request.method == "POST":
        telephone = request.POST.get("telephone")
        username = request.POST.get("username")
        description = request.POST.get("description")

        houseRequirement=HouseRequirement();
        houseRequirement.telephone=telephone
        houseRequirement.name = username
        houseRequirement.description=description

        houseRequirement.save()
        request.session["headSubmit"] = "yes"
        return HttpResponseRedirect(request.GET["returnUrl"])

def aboutus(request):
    return render(request, 'frontsite/aboutus.html', {})

def building(request,id):
    build = OfficeBuildingList.objects.get(pk=id)
    officelist = OfficeList.objects.filter(officeBuilding_id=id)
    buildinglist = OfficeBuildingList.objects.all()[0:4]
    isAppoint="false"
    if request.method == "POST":
        order=Order()
        order.title=build.title
        order.telephone=request.session['login']
        order.officeBuilding_id=build.id
        order.orderid=uuid.uuid1()
        order.status_id=3
        order.save()
        isAppoint="true"
        return render(request, 'frontsite/building.html',
                      {"building": build, "officelist": officelist, "buildinglist": buildinglist,"appoint":"success","isAppoint":isAppoint})

    else:
        if request.session.has_key("login"):
            count = Order.objects.filter(officeBuilding_id=id).filter(telephone=request.session['login']).filter(
                buildingOrService='building').count()
            if (count > 0):
                isAppoint = "true"
        return render(request, 'frontsite/building.html', {"building":build,"officelist":officelist,"buildinglist":buildinglist,"isAppoint":isAppoint})

def buildinglist(request,*args,**kargs):
    print kargs
    for arg in kargs:
        if (kargs[arg] != None) & (arg != "search"):
            kargs[arg]=int(kargs[arg])

    buildinglist=OfficeBuildingList.objects.all()
    if kargs.get("type") != None :
        buildinglist=buildinglist.filter(building_type_id=kargs.get("type"))
    if kargs.get("country") != None :
        buildinglist=buildinglist.filter(area_type_id=kargs.get("country"))
    if kargs.get("district") != None :
        buildinglist=buildinglist.filter(district_type_id=kargs.get("district"))
    if kargs.get("search") != None :
        if kargs.get("search") != "":
            buildinglist=buildinglist.filter(Q(title__icontains=kargs.get("search")) | Q(address__icontains=kargs.get("search")) | Q(transport__icontains=kargs.get("search")))
    if kargs.get("areanum") != None :
        areanum=kargs.get("areanum")
        minvalue=0;
        maxvalue=0;
        if areanum == 1:
            minvalue=0;
            maxvalue=100;
        elif areanum == 2:
            minvalue=100;
            maxvalue=200;
        elif areanum == 3:
            minvalue=200;
            maxvalue=300;
        elif areanum == 4:
            minvalue=300;
            maxvalue=500;
        elif areanum == 5:
            minvalue=500;
            maxvalue=800;
        elif areanum == 6:
            minvalue=800;
            maxvalue=1000;
        else:
            minvalue=1000;
            maxvalue=100000;
        buildinglist = buildinglist.filter(~(Q(rent_min_area__gt=maxvalue)|Q(rent_max_area__lt=minvalue)))
    sourceTypeList=SourceType.objects.all()
    subwayList=Subway.objects.all()
    areaList=Area.objects.all()
    map={"buildinglist":buildinglist,"sourceTypeList":sourceTypeList,"subwayList":subwayList,"areaList":areaList}
    newmap=dict(kargs.items()+map.items())
    if kargs["country"] != None:
        # newmap["districtList"]=District.objects.filter(area_type_id=kargs["country"])
        districtList=District.objects.filter(area_type_id=kargs["country"]).order_by("sort_int")
        for index in range(len(districtList)):
            if index >0:
                if(districtList[index].district_firstChar==districtList[index-1].district_firstChar):
                    districtList[index].district_firstChar=''

        newmap["districtList"]=districtList
    print newmap
    return render(request, 'frontsite/buildinglist.html', newmap)

def contactus(request):
    return render(request, 'frontsite/contactus.html', {})

def enterprise(request):
    if request.session.has_key('login'):
        account = Account.objects.get(telephone=request.session['login'])
        count = Corporation.objects.filter(userid_id=account.id).count()
        if count > 0:
            corporation = Corporation.objects.get(userid_id=account.id)
            return render(request, 'frontsite/enterprise.html', {"corporation":corporation})
        return render(request, 'frontsite/enterprise.html', {})
    else:
        return HttpResponseRedirect('/frontsite/login/?returnUrl=/frontsite/enterprise/')


def enterpriseRegiste(request):
    if request.method == "POST":
        telephone = request.POST.get("telephone")
        servicetype = request.POST.getlist("servicetype")
        content=''
        for s in servicetype:
            content=content+s+','
        print servicetype
        pic1=request.FILES['pic1']
        pic2 = request.FILES['pic2']
        pic1_path=""
        pic2_path=""
        if pic1:
            phototime = request.user.username + str(time.time()).split('.')[0]
            photo_last = str(pic1).split('.')[-1]
            photoname = 'photos/%s.%s' % (phototime, photo_last)
            img = Image.open(pic1)
            img.save('/Users/xieyaxiong/PycharmProjects/SpaceWebsite/pic_folder/' + photoname)
            pic1_path='/pic_folder/' + photoname
        if pic2:
            phototime = request.user.username + str(time.time()).split('.')[0]
            photo_last = str(pic2).split('.')[-1]
            photoname = 'photos/%s.%s' % (phototime, photo_last)
            img = Image.open(pic2)
            img.save('/Users/xieyaxiong/PycharmProjects/SpaceWebsite/pic_folder/' + photoname)
            pic2_path='/pic_folder/' + photoname

        corporation=Corporation()
        corporation.telephone=telephone
        corporation.businessLicence=pic1_path
        corporation.serviceContent=content
        corporation.corporateCharter=pic2_path
        account=Account.objects.get(telephone=request.session['login'])
        corporation.userid_id=account.id
        corporation.save()

        corporation=Corporation.objects.get(userid_id=account.id)
        return render(request, 'frontsite/enterpriseDisplay.html', {"corporation": corporation})

    else:
        if request.session.has_key('login'):
            account = Account.objects.get(telephone=request.session['login'])
            count=Corporation.objects.filter(userid_id=account.id).count()
            if count>0:
                corporation = Corporation.objects.get(userid_id=account.id)
                return render(request, 'frontsite/enterpriseDisplay.html',{"corporation": corporation})
            else:
                serviceTypes=ServiceType.objects.all()
                services=Services.objects.all()
                return render(request, 'frontsite/enterpriseRegiste.html', {"servicetypes":serviceTypes,"services":services})
        else:
            return HttpResponseRedirect('/frontsite/login/?returnUrl=/frontsite/enterpriseRegiste/')

def houseSource(request):
    return render(request, 'frontsite/houseSource.html', {})

def index(request):
    buildinglist=OfficeBuildingList.objects.all()[0:5]
    newlist=list(News.objects.all()[0:13])
    areaList = Area.objects.all()
    return render(request, 'frontsite/index.html', {"newlist":newlist,"arealist":areaList,"buildinglist":buildinglist})


def login(request):
    if request.method == "POST":
        telephone = request.POST.get("telephone")
        password = request.POST.get("password")
        map = {"telephone": telephone, "password": password}
        q = Account.objects.filter(telephone=telephone, password=password)
        if q.count() == 0:
            map["checkError"] = "error"
            map["returnUrl"]=request.GET["returnUrl"]
            return render(request, 'frontsite/login.html', map)

        request.session["login"]=telephone
        request.session["nickname"]=Account.objects.get(telephone=telephone).nickname
        return HttpResponseRedirect(request.GET["returnUrl"])

    else:
        returnUrl = request.GET["returnUrl"]
        if "login" in returnUrl:
            returnUrl = "/frontsite/index/"
        if "registe" in returnUrl:
            returnUrl = "/frontsite/index/"
        return render(request, 'frontsite/login.html', {"returnUrl":returnUrl})

def map(request):
    return render(request, 'frontsite/map.html', {})

def messages(request):
    if request.session.has_key('login'):
        account=Account.objects.get(telephone=request.session['login'])
        messagelist=Messages.objects.filter(toUser_id=account.id).order_by('-id')
        return render(request, 'frontsite/messages.html', {'messagelist':messagelist})
    else:
        return HttpResponseRedirect('/frontsite/login/?returnUrl=/frontsite/messages/')

def deleteMessage(request,id):
    try:
         Messages.objects.get(pk=id).delete()
    except:
        print 'error'
    account = Account.objects.get(telephone=request.session['login'])
    messagelist = Messages.objects.filter(toUser_id=account.id).order_by('-id')
    return render(request, 'frontsite/messages.html', {'messagelist': messagelist})

def new(request,newid):
    new = News.objects.get(pk=newid)
    htmlcontent=new.htmlContent
    if new.image1.name.find('no-img.jpg') ==-1:
        htmlcontent=htmlcontent.replace("[p1]","<img src='/"+new.image1.name+"' />")
    if new.image2.name.find('no-img.jpg') ==-1:
        htmlcontent=htmlcontent.replace("[p2]","<img src='"+new.image2.name+"' />")
    if new.image3.name.find('no-img.jpg') ==-1:
        htmlcontent=htmlcontent.replace("[p3]","<img src='"+new.image3.name+"' />")
    if new.image4.name.find('no-img.jpg') ==-1:
        htmlcontent=htmlcontent.replace("[p4]","<img src='"+new.image4.name+"' />")
    if new.image5.name.find('no-img.jpg') ==-1:
        htmlcontent=htmlcontent.replace("[p5]","<img src='"+new.image5.name+"' />")
    new.htmlContent=htmlcontent
    return render(request, 'frontsite/new.html', {"new":new})

def news(request,type):
    newlist=News.objects.filter(new_type=type)
    return render(request, 'frontsite/news.html', {"newlist":newlist,"type":type})

def oa(request):
    return render(request, 'frontsite/oa.html', {})

def office(request,id):
    office = OfficeList.objects.get(pk=id)
    return render(request, 'frontsite/office.html', {"office":office})

def orders(request,type):
    if request.session.has_key('login'):
        if int(type) == 10:
            orderlist = Order.objects.filter(telephone=request.session['login'])
            return render(request, 'frontsite/orders.html', {'orderlist': orderlist, "type": type})
        else:
            orderlist = Order.objects.filter(telephone=request.session['login']).filter(status_id=type)
            return render(request, 'frontsite/orders.html', {'orderlist': orderlist, "type": type})
    else:
        return HttpResponseRedirect('/frontsite/login/?returnUrl=/frontsite/orders/')


def personal(request):
    if request.session.has_key("login"):
        q = Account.objects.get(telephone=request.session["login"])
        return render(request, 'frontsite/personal.html', {"account":q})
    else:
        return HttpResponseRedirect('/frontsite/login/?returnUrl=/frontsite/personal/')


def publish(request):
    if request.session.has_key('login'):
        return render(request, 'frontsite/publish.html', {})
    else:
        return HttpResponseRedirect('/frontsite/login/?returnUrl=/frontsite/publish/')

def recruitment(request):
    return render(request, 'frontsite/recruitment.html', {})

def registe(request):
    if request.method== "POST":
        telephone=request.POST.get("telephone")
        checkcode=request.POST.get("checkcode")
        password=request.POST.get("password")
        map={"telephone":telephone,"checkcode":checkcode,"password":password,"returnUrl":request.GET["returnUrl"]}
        if request.session.has_key("checkcode") & (request.session["checkcode"]== checkcode):
            q=Account.objects.filter(telephone=telephone)
            if q.count()==1:
                map["telephoneError"]="error"
                return render(request, 'frontsite/registe.html', map)

            account = Account()
            account.telephone = telephone
            account.password = password
            account.nickname = telephone
            account.age=20
            account.save()
            request.session["login"] = telephone
            return HttpResponseRedirect("/frontsite/personal")
        else:
            map["checkcodeError"] = "error"
            return render(request, 'frontsite/registe.html', map)
    else:
        ustring=uuid.uuid1().__str__()
        request.session['token']=ustring
        print 'ssss'
        print ustring
        returnUrl=request.GET["returnUrl"]
        if "login" in returnUrl:
            returnUrl = "/frontsite/index/"
        if "registe" in returnUrl:
            returnUrl = "/frontsite/index/"
        return render(request, 'frontsite/registe.html', {"token":ustring,"returnUrl":returnUrl})

def requirement(request):
    if request.session.has_key('login'):
        return render(request, 'frontsite/requirement.html', {})
    else:
        return HttpResponseRedirect('/frontsite/login/?returnUrl=/frontsite/requirement/')

def service(request,id):
    if request.method == "POST":
        telephone = request.POST.get("telephone")
        username = request.POST.get("username")
        content=request.POST.get("content")
        requireService=ServiceRequirement()
        requireService.name=username
        requireService.telephone=telephone
        requireService.description=content
        requireService.servicetype_id=id
        requireService.save()
        service = Services.objects.get(pk=id)
        return render(request, 'frontsite/service.html', {"service":service,"status":"success"})

    else:
        service=Services.objects.get(pk=id)
        return render(request, 'frontsite/service.html', {"service":service})


def services(request):
    services1=Services.objects.filter(service_type_id=1)
    services2 = Services.objects.filter(service_type_id=2)
    services3 = Services.objects.filter(service_type_id=3)
    return render(request, 'frontsite/services.html', {"services1":services1,"services2":services2,"services3":services3})

def mysourse(request):
    return render(request, 'frontsite/mysourse.html', {})

def sendcheckcode(request):
        if request.session.has_key("token"):
            print request.session["token"]
        else:
            return HttpResponse("fail")

        stoken= request.session["token"]
        telephone = request.GET.get('telephone')
        token = request.GET.get('token')
        count=0
        print telephone
        print token
        if stoken== token:
            if request.session.has_key("sendcount"):
                count=request.session["sendcount"];

            if count>30:
                return HttpResponse("fail")
            count = count + 1
            request.session["sendcount"]=count
            checkcode=str(random.randrange(0,9))+str(random.randrange(0,9))+str(random.randrange(0,9))
            print checkcode
            request.session["checkcode"]=checkcode
            return HttpResponse("success")
        else:
            return HttpResponse("fail")

def captcha(request):
    '''Captcha'''
    image = Image.new('RGB', (147, 49), color = (255, 255, 255)) # model, size, background color
    font_file = os.path.join(BASE_DIR, 'static/Arial.ttf') # choose a font file
    font = ImageFont.truetype(font_file, 47) # the font object
    draw = ImageDraw.Draw(image)
    rand_str = ''.join(random.sample(string.letters + string.digits, 4)) # The random string
    draw.text((7, 0), rand_str, fill=(0, 0, 0), font=font) # position, content, color, font
    del draw
    request.session['captcha'] = rand_str.lower() # store the content in Django's session store
    buf = cStringIO.StringIO() # a memory buffer used to store the generated image
    image.save(buf, 'jpeg')
    return HttpResponse(buf.getvalue(), 'image/jpeg') # return the image data stream as image/jpeg format, browser will treat it as an image





def test(request):
    context = {"nav_flag": 4}
    return render(request, 'frontsite/bak/services.html', context)


def page_not_found(request):
    return render(request,'frontsite/404.html',{})

def page_error(request):
    return render(request,'frontsite/404.html',{})



def updatePersonal(request):
    if request.method == "POST":
        q = Account.objects.get(telephone=request.session["login"])
        nickname = request.POST.get("nickname")
        realname=request.POST.get("realname")
        sex=request.POST.get("sex")
        address=request.POST.get("address")

        if nickname:
            q.nickname=nickname
            q.save()
        if realname:
            q.realname=realname
            q.save()
        if sex:
            q.sex_id=int(sex)
            q.save()
        if address:
            q.address=address
            q.save()

        return render(request, 'frontsite/personal.html', {"account": q})

