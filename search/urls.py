from django.conf.urls import url
from .views import do_search_for_sale, do_search_sold, do_search_despatched

urlpatterns = [
    url(r'^search_for_sale$', do_search_for_sale, name='do_search_for_sale'),
    url(r'^search_sold$', do_search_sold, name='do_search_sold'),
    url(r'^search_despatched$', do_search_despatched,
        name='do_search_despatched'),
]
