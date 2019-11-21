from django.conf.urls import url
from .views import checkout

urlpatterns = [
    url(r'^(?P<id>\d+)/$', checkout, name='checkout'),
]