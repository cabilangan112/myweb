# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.conf import settings
from django.db import models
from django.db.models.signals import pre_save
from django.core.urlresolvers import reverse
from locations.utils import unique_slug_generator
from locations.models import Location
User = settings.AUTH_USER_MODEL


class Item(models.Model):
	User					= models.ForeignKey(User)
	Location				= models.ForeignKey(Location)
	Category
	Item_name				= models.CharField(max_length=120)
	