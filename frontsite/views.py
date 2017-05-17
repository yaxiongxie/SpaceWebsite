from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

from .models import Rent, OfficeBuilding, Country, Subway,User
from .forms import UserForm


def buildinglist(reqest, country_id, subway_id, area_id, price_id):
    country_id = int(country_id)
    subway_id = int(subway_id)
    area_id = int(area_id)
    price_id = int(price_id)
    country_list = Country.objects.all()
    subway_list = Subway.objects.all()

    data_list=OfficeBuilding.objects.filter(status__in=(1,3))
    if country_id != 0:
        data_list=data_list.filter(country=country_id)
    if subway_id != 0:
        data_list = data_list.filter(subway=subway_id)

    if price_id != 0:
        if price_id == 1:
            data_list = data_list.filter(rent_price__range=(0, 3))
        if price_id == 2:
            data_list = data_list.filter(rent_price__range=(3, 5))
        if price_id == 3:
            data_list = data_list.filter(rent_price__range=(5, 10))
        if price_id == 4:
            data_list = data_list.filter(rent_price__range=(10, 15))
        if price_id == 5:
            data_list = data_list.filter(rent_price__range=(15, 100000))

    if area_id != 0:
        if area_id == 1:
            data_list = data_list.filter(totalArea__range=(0, 100))
        if area_id == 2:
            data_list = data_list.filter(totalArea__range=(100, 300))
        if area_id == 3:
            data_list = data_list.filter(totalArea__range=(300, 500))
        if area_id == 4:
            data_list = data_list.filter(totalArea__range=(500, 1000))
        if area_id == 5:
            data_list = data_list.filter(totalArea__range=(1000, 2000))
        if area_id == 6:
            data_list = data_list.filter(totalArea__range=(2000, 1000000))

    context = {'country_list': country_list, 'subway_list': subway_list, 'data_list': data_list, "nav_flag": 2}
    context['country_id'] = country_id
    context['subway_id'] = subway_id
    context['area_id'] = area_id
    context['price_id'] = price_id
    return render(reqest, 'frontsite/building_list.html', context)


def rentlist(reqest, country_id, subway_id, rent_id, area_id, type_id):
    country_id = int(country_id)
    subway_id = int(subway_id)
    rent_id = int(rent_id)
    area_id = int(area_id)
    type_id = int(type_id)
    country_list = Country.objects.all()
    subway_list = Subway.objects.all()

    kwargs = {
        'status__id': 1
    }
    if country_id != 0:
        kwargs['country__id'] = country_id
    if subway_id != 0:
        kwargs['subway_id'] = subway_id
    if type_id != 0:
        kwargs['roomType'] = type_id

    data_list = Rent.objects.filter(**kwargs)

    if rent_id != 0:
        if rent_id == 1:
            data_list = data_list.filter(price__range=(0, 1000))
        if rent_id == 2:
            data_list = data_list.filter(price__range=(1000, 2000))
        if rent_id == 3:
            data_list = data_list.filter(price__range=(2000, 3000))
        if rent_id == 4:
            data_list = data_list.filter(price__range=(3000, 5000))
        if rent_id == 5:
            data_list = data_list.filter(price__range=(5000, 100000))

    if area_id != 0:
        if area_id == 1:
            data_list = data_list.filter(area__range=(0, 50))
        if area_id == 2:
            data_list = data_list.filter(area__range=(50, 70))
        if area_id == 3:
            data_list = data_list.filter(area__range=(70, 90))
        if area_id == 4:
            data_list = data_list.filter(area__range=(90, 120))
        if area_id == 5:
            data_list = data_list.filter(area__range=(120, 140))
        if area_id == 6:
            data_list = data_list.filter(area__range=(140, 160))
        if area_id == 7:
            data_list = data_list.filter(area__range=(160, 200))
        if area_id == 8:
            data_list = data_list.filter(area__range=(200, 100000))

    context = {'country_list': country_list, 'subway_list': subway_list, 'data_list': data_list, "nav_flag": 3}
    context['country_id'] = country_id
    context['subway_id'] = subway_id
    context['rent_id'] = rent_id
    context['area_id'] = area_id
    context['type_id'] = type_id
    return render(reqest, 'frontsite/rent_list.html', context)


def buildingdetail(request, id):
    building = OfficeBuilding.objects.get(pk=id)
    context = {"nav_flag": 2, "building": building}
    return render(request, 'frontsite/building_detail.html', context)


def rentdetail(request, id):
    rent = Rent.objects.get(pk=id)
    context = {"nav_flag": 3, "rent": rent}
    return render(request, 'frontsite/rent_detail.html', context)


def aboutus(request):
    context = {"nav_flag": 5}
    return render(request, 'frontsite/aboutus.html', context)


def index(request):
    country_list = Country.objects.all()
    data_list = OfficeBuilding.objects.filter(status=3)
    context = {"nav_flag": 1,"country_list":country_list,"building_list":data_list}
    return render(request, 'frontsite/index.html', context)


def services(request):
    context = {"nav_flag": 4}
    return render(request, 'frontsite/services.html', context)


def addForm(request):
    if request.method== 'POST':
        u = UserForm(request.POST)
        if u.is_valid():
            u.save()

        else:
            print 'error'
            return render(request, 'frontsite/addForm.html', {"error": u.errors})

    return render(request, 'frontsite/addForm.html', {})