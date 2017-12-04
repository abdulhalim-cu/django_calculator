from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^ajax_rate/$', views.ajax_rate, name='ajax_rate'),
]