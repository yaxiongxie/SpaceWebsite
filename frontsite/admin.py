from django.contrib import admin

from .models import Account,HouseSource,HouseRequirement,ServiceRequirement,Order,Corporation,Messages

# class OfficeBuildingAdmin(admin.ModelAdmin):
#     list_display = ('title', 'createTime')
#     list_filter = ['createTime']
#
#     class Media:
#         js = (
#             'kindeditor/kindeditor-all.js',
#             'kindeditor/lang.zh_CN.js',
#             'kindeditor/config.js',
#         )
#
#
# class RentAdmin(admin.ModelAdmin):
#     list_display = ('title', 'createTime')
#     liast_filter = ['createTime']
#
# admin.site.register(Country)
# admin.site.register(Subway)
# admin.site.register(RoomType)
# admin.site.register(CmsStatus)
# admin.site.register(RoomDirection)
# admin.site.register(OfficeBuilding, OfficeBuildingAdmin)
# admin.site.register(Rent, RentAdmin)


admin.site.register(Account)
admin.site.register(HouseSource)
admin.site.register(HouseRequirement)
admin.site.register(ServiceRequirement)
admin.site.register(Order)
admin.site.register(Corporation)
admin.site.register(Messages)


