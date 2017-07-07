# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
# -*- coding: utf-8 -*-

from django.contrib import admin

# Register your models here.
from django.contrib import admin

from .models import OfficeBuildingList,OfficeList,News


class NewAdmin(admin.ModelAdmin):

    class Media:
        js = (
            'kindeditor/kindeditor-all.js',
            'kindeditor/lang.zh_CN.js',
            'kindeditor/config.js',
        )


class OfficeBuildingListAdmin(admin.ModelAdmin):
    list_display = ('title','area_type','district_type', 'createTime')
    list_filter = ['createTime']
    search_fields = ['title','area_type__country_name','district_type__district_name']
    raw_id_fields = ('district_type',)

class OfficeListAdmin(admin.ModelAdmin):
    list_display = ('title','officeBuilding','ownerName','ownerTelephone', 'createTime')
    list_filter = ['createTime']
    search_fields = ['title']
    raw_id_fields = ('officeBuilding',)


admin.site.register(OfficeBuildingList,OfficeBuildingListAdmin)
admin.site.register(OfficeList,OfficeListAdmin)
admin.site.register(News,NewAdmin)


