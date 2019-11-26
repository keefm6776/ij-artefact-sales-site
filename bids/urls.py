from django.conf.urls import url
from .views import make_bid
from artefacts.models import Artefact

urlpatterns = [
    url(r'^(?P<pk>\d+)/bid/$', make_bid, name='make_bid')
    ]