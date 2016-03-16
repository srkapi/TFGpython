from django.conf.urls import url, include
from app.views import index, measure

urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^measure/$', measure, name='urlname')
]