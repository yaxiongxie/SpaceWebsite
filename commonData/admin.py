# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from django.contrib import admin

from .models import Subway,Area,District,SourceType,UseType,DecorateDegree,NewType,Sex,Status,ServiceType,Services

class DistrictAdmin(admin.ModelAdmin):
    list_display = ('district_name','area_type')


admin.site.register(Subway)
admin.site.register(Area)
admin.site.register(District,DistrictAdmin)
admin.site.register(SourceType)
admin.site.register(UseType)
admin.site.register(DecorateDegree)
admin.site.register(NewType)
admin.site.register(Sex)
admin.site.register(Status)
admin.site.register(ServiceType)
admin.site.register(Services)


