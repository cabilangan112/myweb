# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.mixins import (
	LoginRequiredMixin,
	PermissionRequiredMixin
	)
from .forms import LostUpdateForm
from django.views import generic
from django.shortcuts import render
from models import ItemLost, OwnerInfo,LocationLost,ReturnerInfo
from django.views.generic import (ListView,DetailView,CreateView,UpdateView)

 
 
class ItemLost_View(generic.ListView):
	def get(self, request): 
		query = self.request.GET.get('q')
		item_exists = ItemLost.objects.filter(Returned=False).order_by("-Updated")[:10].exists()
		item = ItemLost.objects.all() 
		pl = LocationLost.objects.all() 
		of = OwnerInfo.objects.all() 
		ri = ReturnerInfo.objects.all() 

		if item_exists and pl.exists():
			return render(request, "Item_lost_list.html", {'object_list':item})
			return render(request, "Item_lost_list.html", {'object_list':pl})
			return render(request, "Item_lost_list.html", {'object_list':of})
			return render(request, "Item_lost_list.html", {'object_list':ri})
			
		return render(request, "Item_lost_list.html", {'object_list':item})
		return render(request, "Item_lost_list.html", {'object_list':pl})
		return render(request, "Item_lost_list.html", {'object_list':of})
		return render(request, "Item_lost_list.html", {'object_list':ri})
		
		
class LostDetail(LoginRequiredMixin, DetailView):
	def get_queryset(self):
		return Item.objects.filter(user=self.request.user)


class ReturnedView(ListView):
	def get(self, request, *args, **kwargs):
		if not request.user.is_authenticated():
			return render(request, "index.html", {})
		qs = ItemLost.objects.filter(Returned=True).order_by("-updated")[:10]
		return render(request, " ", {'object_list':qs})

class LostUpdate(UpdateView):
	form_class = LostUpdateForm
	template_name = 'items/detail-update.html'
	
	def get_queryset(self):
		return ItemLost.objects.filter(user=self.request.user)

	# context for html title
	def get_context_data(self, *args, **kwargs):
		context = super(LostUpdate, self).get_context_data(*args, **kwargs)
		context['title'] = 'Update Item'
		return context

	#for user checking if login of not
	#giving data
	def get_form_kwargs(self):
		kwargs = super(LostUpdate, self).get_form_kwargs()
		kwargs['User'] = self.request.user
		return kwargs
		
class ItemListView(LoginRequiredMixin, ListView):
	def get_queryset(self):
		return Item.objects.filter(user=self.request.user)