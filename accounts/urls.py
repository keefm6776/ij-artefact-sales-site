from django.conf.urls import url, include
from django.contrib import admin
from . import urls_reset
from .views import index, register, logout, login
from .views import profile

urlpatterns = [
    url(r'^register/$', register, name='register'),
    url(r'^profile/(?P<id>\d+)/$', profile, name='profile'),
    url(r'^logout/$', logout, name='logout'),
    url(r'^login/$', login, name='login'),
    url(r'^password-reset/', include(urls_reset)),
    ]
