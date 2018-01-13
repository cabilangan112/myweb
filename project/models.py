# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.conf import settings
from django.db import models
from django.db.models.signals import pre_save
from django.core.urlresolvers import reverse
#from locations.utils import unique_slug_generator
#from locations.models import Location
User = settings.AUTH_USER_MODEL


class ItemLost(models.Model):
	User					= models.ForeignKey(User)
	Category				= models.CharField(max_length=120)
	Item_name				= models.CharField(max_length=120)
	item_picture			= models.ImageField(upload_to = 'static/media')#, default = 'pic_folder/None/no-img.jpg')
	Item_description 		= models.TextField(help_text='Item Description', null=True, blank=True)
	Lost_place				= models.CharField(max_length=120) 
	Date_Lost				= models.DateTimeField(auto_now_add=True)
	Value 					= models.IntegerField(null=True)
	Timestamp				= models.DateTimeField(auto_now_add=True)
	Updated					= models.DateTimeField(auto_now=True)
	Owner 					= models.ForeignKey('OwnerInfo', on_delete=models.SET_NULL, null=True)
	
	def __str__(self):
		return self.Item_name

	class Meta:
		ordering = ['-Updated', '-Timestamp']

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
	Course     				= models.CharField(max_length=120)
	Year 					= models.CharField(max_length=120)
	
	def get_absolute_url(self):
		return reverse(' owner-detail', args=[str(self.id)])

	def __str__(self):
		return '%s, %s' % (self.Last_name, self.First_name)

	
	
	