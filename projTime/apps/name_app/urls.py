from django.conf.urls import url
from . import views      

urlpatterns = [
    url(r'^$', views.index),     
    url(r'^name_app$', views.index)
]