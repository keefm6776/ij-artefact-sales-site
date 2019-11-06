from django.conf.urls import url, include
from django.contrib import admin
from . import urls_reset
from .views import index, register, profile, logout, login
from customer.views import CreateProfileView, DisplayDetailView

urlpatterns = [
    url(r'^register/$', register, name='register'),
    url(r'^profile/$', profile, name='profile'),
    url(r'^logout/$', logout, name='logout'),
    url(r'^login/$', login, name='login'),
    url(r'^password-reset/', include(urls_reset)),
    url(r'^create', CreateProfileView.as_view(), name='create'),
    url(r'^detail/<pk>', DisplayDetailView.as_view(),name='profile-detail')
]
