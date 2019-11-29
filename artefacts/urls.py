from django.conf.urls import url
from .views import for_sale_artefacts, artefact_detail, add_artefact, edit_artefact_detail, delete_artefact, sold_artefacts, despatched_artefacts, despatch_artefact

urlpatterns = [
    url(r'^for_sale/$', for_sale_artefacts, name='for_sale_artefacts'),
    url(r'^sold/$', sold_artefacts, name='sold_artefacts'),
    url(r'^despatched/$', despatched_artefacts, name='despatched_artefacts'),
    url(r'^detail/(?P<pk>\d+)/$', artefact_detail, name='artefact_detail'),
    url(r'^add/$', add_artefact, name='add_artefact'),
    url(r'^edit/(?P<id>\d+)/$', edit_artefact_detail, name='edit_artefact_detail'),
    url(r'^delete/(?P<id>\d+)/$', delete_artefact, name='delete_artefact'),
    url(r'^despatch/(?P<id>\d+)/$', despatch_artefact, name='despatch_artefact'),
     ]
