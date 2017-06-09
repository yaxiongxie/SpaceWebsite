from django.shortcuts import render,HttpResponseRedirect
from PIL import Image, ImageDraw, ImageFont
from django.http.response import HttpResponse
from SpaceWebsite.settings import BASE_DIR
import cStringIO, string, os, random
import json
import uuid
from models import Account


def aboutus(request):
    return render(request, 'frontsite/aboutus.html', {})

def building(request):
    return render(request, 'frontsite/building.html', {})

def buildinglist(request):
    return render(request, 'frontsite/buildinglist.html', {})

def contactus(request):
    return render(request, 'frontsite/contactus.html', {})

def enterprise(request):
    return render(request, 'frontsite/enterprise.html', {})

def enterpriseRegiste(request):
    return render(request, 'frontsite/enterpriseRegiste.html', {})

def houseSource(request):
    return render(request, 'frontsite/houseSource.html', {})

def index(request):
    return render(request, 'frontsite/index.html', {})


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
        return HttpResponseRedirect(request.GET["returnUrl"])

    else:
        return render(request, 'frontsite/login.html', {"returnUrl":request.GET["returnUrl"]})

def map(request):
    return render(request, 'frontsite/map.html', {})

def messages(request):
    return render(request, 'frontsite/messages.html', {})


def new(request):
    return render(request, 'frontsite/new.html', {})

def news(request):
    return render(request, 'frontsite/news.html', {})

def oa(request):
    return render(request, 'frontsite/oa.html', {})

def office(request):
    return render(request, 'frontsite/office.html', {})

def orders(request):
    return render(request, 'frontsite/orders.html', {})

def personal(request):
    return render(request, 'frontsite/personal.html', {})

def publish(request):
    return render(request, 'frontsite/publish.html', {})

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
        return render(request, 'frontsite/registe.html', {"token":ustring,"returnUrl":request.GET["returnUrl"]})

def requirement(request):
    return render(request, 'frontsite/requirement.html', {})

def service(request):
    return render(request, 'frontsite/service.html', {})

def services(request):
    return render(request, 'frontsite/services.html', {})

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

