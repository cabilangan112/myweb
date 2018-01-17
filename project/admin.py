# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import ItemLost, OwnerInfo, LocationLost,ReturnerInfo

# Register your models here.

class ItemLostAdmin(admin.ModelAdmin):
    list_display = ('Item_name', 'Category', 'image', 'Item_description','Location','Value','Time','Updated',)

	
	
	
	
admin.site.register(ItemLost,ItemLostAdmin)
admin.site.register(OwnerInfo)
admin.site.register(LocationLost)
admin.site.register(ReturnerInfo)
