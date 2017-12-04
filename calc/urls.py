from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^ajax_rate/(?P<media>[a-zA-Z0-9]+)/(?P<customer>[a-zA-Z]+)/(?P<square_feet>[0-9]+)/$', 
    	views.ajax_rate, name='ajax_rate'),
]