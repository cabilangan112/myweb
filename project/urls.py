from django.conf.urls import url
from django.utils import timezone
from . import views
from django.views.generic import DetailView, ListView, UpdateView
from models import ItemLost



urlpatterns = [
	url(r'^$',ListView.as_view(queryset=ItemLost.objects.filter(Updated__lte=timezone.now()).order_by('Updated')[:10],context_object_name='LItem', template_name='Item_lost_list.html'), name='ItemLost_list'),
	
]