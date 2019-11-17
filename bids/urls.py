from django.conf.urls import url
from .views import make_bid

urlpatterns = [
    #url(r'^$', get_bids, name='get_bids'),
    url(r'new/$', make_bid, name='make_bid'),
     ]
