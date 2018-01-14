# -*- coding: utf-8 -*-
from __future__ import unicode_literals



from django.views import generic
from django.shortcuts import render
from models import ItemLost, OwnerInfo,LocationLost,ReturnerInfo
from django.views.generic import (ListView,DetailView,CreateView,UpdateView)

 
class indexView(ListView):
	def get(self, request, *args, **kwargs):
		if not request.user.is_authenticated():
			return render(request, "index", {})
		qs = ItemLost.objects.filter(Returned=False).order_by("-updated")[:10]
		return render(request, " ", {'object_list':qs})

		
class ReturnedView(ListView):
	def get(self, request, *args, **kwargs):
		if not request.user.is_authenticated():
			return render(request, "home.html", {})
		qs = ItemLost.objects.filter(Returned=True).order_by("-updated")[:10]
		return render(request, " ", {'object_list':qs})
		
		
