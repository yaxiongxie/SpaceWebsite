"""Django URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from . import views

urlpatterns = [
url(r'^test/', views.test),

url(r'^aboutus/', views.aboutus),
url(r'^building/', views.building),
url(r'^buildinglist/', views.buildinglist),
url(r'^contactus/', views.contactus),
url(r'^enterprise/', views.enterprise),
url(r'^enterpriseRegiste/', views.enterpriseRegiste),
url(r'^houseSource/', views.houseSource),
url(r'^index/', views.index),
url(r'^login/', views.login),
url(r'^map/', views.map),
url(r'^messages/', views.messages),
url(r'^new/', views.new),
url(r'^news/', views.news),
url(r'^oa/', views.oa),
url(r'^office/', views.office),
url(r'^orders/', views.orders),
url(r'^personal/', views.personal),
url(r'^publish/', views.publish),
url(r'^recruitment/', views.recruitment),
url(r'^registe/', views.registe),
url(r'^requirement/', views.requirement),
url(r'^service/', views.service),
url(r'^services/', views.services),
url(r'^mysourse/', views.mysourse),



]
