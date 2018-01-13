# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import ItemLost, OwnerInfo, LocationLost,ReturnerInfo

# Register your models here.
admin.site.register(ItemLost)
admin.site.register(OwnerInfo)
admin.site.register(LocationLost)
admin.site.register(ReturnerInfo)
