from django.shortcuts import render


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
    return render(request, 'frontsite/login.html', {})

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
    return render(request, 'frontsite/registe.html', {})

def requirement(request):
    return render(request, 'frontsite/requirement.html', {})

def service(request):
    return render(request, 'frontsite/service.html', {})

def services(request):
    return render(request, 'frontsite/services.html', {})

def mysourse(request):
    return render(request, 'frontsite/mysourse.html', {})










def test(request):
    context = {"nav_flag": 4}
    return render(request, 'frontsite/bak/services.html', context)

