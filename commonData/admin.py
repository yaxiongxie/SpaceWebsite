# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from django.contrib import admin

from .models import Subway,Area,District,SourceType,UseType,DecorateDegree,NewType,Sex,Status


admin.site.register(Subway)
admin.site.register(Area)
admin.site.register(District)
admin.site.register(SourceType)
admin.site.register(UseType)
admin.site.register(DecorateDegree)
admin.site.register(NewType)
admin.site.register(Sex)
admin.site.register(Status)


