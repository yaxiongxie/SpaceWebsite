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
    url(r'^rentlist/c(\d+)s(\d+)r(\d+)a(\d+)t(\d+)/$', views.rentlist),
    url(r'^buildinglist/c(\d+)s(\d+)a(\d+)p(\d+)/$', views.buildinglist),
    url(r'^rentdetail/(\d+)/$', views.rentdetail),
    url(r'^buildingdetail/(\d+)/$', views.buildingdetail),
    url(r'^aboutus/', views.aboutus),
    url(r'^index/', views.index),
    url(r'^services/', views.services),
    url(r'^form/', views.addForm)
]
