from django.conf.urls import url
 
from .views import (
	ItemLost_View)




urlpatterns = [
	url(r'^$', ItemLost_View.as_view(), name='ItemLost'),

	
]