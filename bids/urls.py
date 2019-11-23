from django.conf.urls import url
from .views import make_bid
from artefacts.models import Artefact

urlpatterns = [
    #url(r'^$', get_bids, name='get_bids'),
    url(r'^(?P<pk>\d+)/bid/$', make_bid, name='make_bid')
    #url(r'new/$', make_bid, name='make_bid'),
    #url(r'^new/(?P<id>\d+)/$', make_bid, name='make_bid'),
     ]