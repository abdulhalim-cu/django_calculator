from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    #url(r'^ajax_rate_request/$', 'ajax_rate_request'),
]