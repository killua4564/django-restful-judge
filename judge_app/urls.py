from django.conf.urls import url, include
from rest_framework import routers
from . import views

urlpatterns = [
    url(r'^new/$', views.newuser),
    url(r'^(?P<userID>[0-9]+)/$', views.username),
    url(r'^(?P<userID>[0-9]+)/delete/$', views.user),
]