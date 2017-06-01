# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
# -*- coding: utf-8 -*-

from django.contrib import admin

# Register your models here.
from django.contrib import admin

from .models import OfficeBuildingList,OfficeList,News

admin.site.register(OfficeBuildingList)
admin.site.register(OfficeList)
admin.site.register(News)


