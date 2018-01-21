from django.conf.urls import url
 
from .views import (
	ItemLost_View,
	Returned_View,
	LostUpdate,
	LostDetail
	)




urlpatterns = [
	url(r'^$', ItemLost_View.as_view(), name='Lost'),
	url(r'^returned/$', Returned_View.as_view(), name='Returned'),
	url(r'^Lost-detail/(?P<pk>\d+)$', LostDetail.as_view(), name='Item-detail'),
	url(r'^(?P<slug>[\w-]+)/$', LostUpdate.as_view(), name='edit'),
	

	
]