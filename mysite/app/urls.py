from django.conf.urls import url, include
from app.views import index, measure,measureAdd

urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^measureadd/$', measureAdd, name='urlname'),
    url(r'^measure/$', measure, name='data')
]