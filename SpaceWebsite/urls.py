"""SpaceWebsite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
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
from django.conf.urls import url,include
from django.contrib import admin
import django
from django.conf.urls import handler404, handler500
from frontsite import views

handler404=views.page_not_found
handler500=views.page_error

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^frontsite/', include('frontsite.urls')),
    url(r'^pic_folder/(?P<path>.*)', django.views.static.serve, {'document_root':'/Users/xieyaxiong/PycharmProjects/SpaceWebsite/pic_folder'}),

]
