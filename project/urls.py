from django.conf.urls import url
from django.utils import timezone
from . import views
from django.views.generic import DetailView, ListView, UpdateView
from models import ItemLost



urlpatterns = [
	url(r'^$',ListView.as_view(queryset=ItemLost.objects.filter(Updated__lte=timezone.now()).order_by('Updated')[:5],context_object_name='ItemLostView', template_name='ItemLost_list.html'), name='ItemLost_list'),
]