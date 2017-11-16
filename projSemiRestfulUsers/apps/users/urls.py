from django.conf.urls import url
from . import views 

urlpatterns = [
  url(r'^$', views.index),  
  url(r'^users$', views.index),
  url(r'^users/new$', views.new),
  url(r'^users/create$', views.create),
  url(r'^users/show/(?P<number>\d+)$', views.show), 
  url(r'^users/edit/(?P<number>\d+)$', views.edit),
  url(r'^users/update/(?P<number>\d+)$', views.update), 
  url(r'^users/delete/(?P<number>\d+)$', views.delete),
]    