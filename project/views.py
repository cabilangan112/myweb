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
		obj = ItemLost.objects.filter(Returned=False).order_by("-Updated")[:10].exists()
		obj = ItemLost.objects.all() 
		context = {
				'obj':obj,
			}
		return render(request, "Item_lost_list.html", context)
		
class LostDetail(DetailView):
	model = ItemLost
	template_name = "Item_Detail.html"	
	def get_context_data(self, **kwargs):
		context = super(LostDetail, self).get_context_data(**kwargs)
		return context


class Returned_View(ListView):
	def get(self, request): 
		query = self.request.GET.get('q')
		obj = ItemLost.objects.filter(Returned=True).order_by("-Updated")[:10].exists()
		obj = ItemLost.objects.all() 
		context = {
				'obj':obj,
			}
		return render(request, "Returned.html", context)
		
class LostUpdate(UpdateView):
	form_class = LostUpdateForm
	template_name = 'items/detail-update.html'
	
	def get_queryset(self):
		return ItemLost.objects.filter(User=self.request.User)

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