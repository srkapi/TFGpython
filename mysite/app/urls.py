from django.conf.urls import url, include
from app.views import *



urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^measureadd/$', measureAdd, name='urlname'),
    url(r'^measure/$', measure, name='data'),
    url(r'^login/$', login_user , name='login'),
    url(r'^logout/$', logout_user, name='logout'),
    url(r'^user/$', list_user, name='user'),
    url(r'^user/new/', user_new, name='user_new'),
    url(r'^udpateUser/', updateUser, name='updateUser'),
    url(r'^deleteUser/', deleteUser, name='deleteUser'),
]