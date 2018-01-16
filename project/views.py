# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.mixins import (
	LoginRequiredMixin,
	PermissionRequiredMixin
	)

from django.views import generic
from django.shortcuts import render
from models import ItemLost, OwnerInfo,LocationLost,ReturnerInfo
from django.views.generic import (ListView,DetailView,CreateView,UpdateView)

 
 
class ItemLost_View(generic.ListView):
	def get(self, request): 
		qs = ItemLost.objects.filter(Returned=False).order_by("-Updated")[:10]
		obj = ItemLost.objects.all()
		context = {
			'obj':obj,
		
		}
		return render(request, "Item_lost_list.html", context)


		
class ReturnedView(ListView):
	def get(self, request, *args, **kwargs):
		if not request.user.is_authenticated():
			return render(request, "index.html", {})
		qs = ItemLost.objects.filter(Returned=True).order_by("-updated")[:10]
		return render(request, " ", {'object_list':qs})
		
		
class ItemListView(LoginRequiredMixin, ListView):
	def get_queryset(self):
		return Item.objects.filter(user=self.request.user)