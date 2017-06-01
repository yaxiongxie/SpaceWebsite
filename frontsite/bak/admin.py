from django.contrib import admin

from .models import OfficeBuilding, Rent,Country,Subway,RoomDirection,RoomType,CmsStatus


class OfficeBuildingAdmin(admin.ModelAdmin):
    list_display = ('title', 'createTime')
    list_filter = ['createTime']

    class Media:
        js = (
            'kindeditor/kindeditor-all.js',
            'kindeditor/lang.zh_CN.js',
            'kindeditor/config.js',
        )


class RentAdmin(admin.ModelAdmin):
    list_display = ('title', 'createTime')
    list_filter = ['createTime']

admin.site.register(Country)
admin.site.register(Subway)
admin.site.register(RoomType)
admin.site.register(CmsStatus)
admin.site.register(RoomDirection)
admin.site.register(OfficeBuilding, OfficeBuildingAdmin)
admin.site.register(Rent, RentAdmin)


