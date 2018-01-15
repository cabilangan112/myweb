# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.conf import settings
from django.db import models
from django.db.models.signals import pre_save
from django.core.urlresolvers import reverse
from datetime import date
from datetime import time
 
 
User = settings.AUTH_USER_MODEL


class ItemLost(models.Model):
	User					= models.ForeignKey(User)
	Category				= models.CharField(max_length=120)
	Item_name				= models.CharField(max_length=120)
	item_picture			= models.ImageField(upload_to = 'static/media')
	Item_description 		= models.TextField(help_text='Item Description', null=True, blank=True)
	Location                = models.ForeignKey('LocationLost', on_delete=models.SET_NULL, null=True)
	Value 					= models.DecimalField('Peso amount', max_digits=8, decimal_places=2, blank=True, null=True)
	Time					= models.DateTimeField(auto_now_add=True)
	Updated					= models.DateTimeField(auto_now=True)
	Owner 					= models.ForeignKey('OwnerInfo', on_delete=models.SET_NULL, null=True)
	Returned				= models.BooleanField(default=False)
	Returner                = models.ForeignKey('ReturnerInfo', on_delete=models.SET_NULL, null=True)
	slug					= models.SlugField(null=True, blank=True)
	
	def __str__(self):
		return self.Item_name

	class Meta:
		ordering = ['-Updated', '-Time']

	def get_item(self):
		return self.item_description.split(",")

	def get_absolute_url(self):
		return reverse('items:edit', kwargs={'slug': self.slug})

	@property
	def title(self):
		return self.Item_name

def rl_pre_save_receiver(sender, instance, *args, **kwargs):
	if not instance.slug:
		instance.slug = unique_slug_generator(instance)

pre_save.connect(rl_pre_save_receiver, sender=ItemLost)


class OwnerInfo(models.Model):
	Last_name 				= models.CharField(max_length=120)
	First_name 				= models.CharField(max_length=120)
	Course_or_Stran    		= models.CharField(max_length=120)
	Year 					= models.CharField(max_length=120)
	
	def get_absolute_url(self):
		return reverse(' owner-detail', args=[str(self.id)])

	def __str__(self):
		return '%s, %s' % (self.Last_name, self.First_name)
		
class LocationLost(models.Model):
	Lost_place				= models.CharField(max_length=120) 
	Date_Lost				= models.DateField(default=date.today)
	Time_lost				= models.TimeField(null=True, blank=True)
	
	
	def get_absolute_url(self):
		return reverse(' locationlost-detail', args=[str(self.id)])

	def __str__(self):
		return '%s, %s' % (self.Lost_place, self.Date_Lost)
		
		
class ReturnerInfo(models.Model):
	Last_name 				= models.CharField(max_length=120)
	First_name 				= models.CharField(max_length=120)
	Course_or_Stran     	= models.CharField(max_length=120)
	Year 					= models.CharField(max_length=90)
	Email                   = models.EmailField(max_length=90)
	
	def get_absolute_url(self):
		return reverse(' Returner-detail', args=[str(self.id)])

	def __str__(self):
		return '%s, %s' % (self.Last_name, self.First_name)
	