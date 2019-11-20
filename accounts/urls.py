from django.conf.urls import url, include
from django.contrib import admin
from . import urls_reset
from .views import index, register, logout, login
from .views import profile
##from customer.views import CreateCustomerView, CustomerDetailView

urlpatterns = [
    url(r'^register/$', register, name='register'),
    ##url(r'^detail/<pk>', CustomerDetailView,name='customer-detail'),
    url(r'^profile/(?P<id>\d+)/$', profile, name='profile'),
#    url(r'^profile/$', profile, name='profile'),
    url(r'^logout/$', logout, name='logout'),
    url(r'^login/$', login, name='login'),
    url(r'^password-reset/', include(urls_reset)),
    ]
