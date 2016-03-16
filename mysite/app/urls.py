from django.conf.urls import url, include
from rest_framework import routers
from app.views import UserViewSet,GroupViewSet

urlpatterns = [
    url(r'^$', views.index, name='index'),
]