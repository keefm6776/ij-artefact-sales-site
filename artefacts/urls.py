from django.conf.urls import url
from .views import all_artefacts, artefact_detail, add_artefact, edit_artefact_detail, delete_artefact, sold_artefacts

urlpatterns = [
    url(r'^all/$', all_artefacts, name='all_artefacts'),
    url(r'^sold/$', sold_artefacts, name='sold_artefacts'),
    url(r'^(?P<pk>\d+)/$', artefact_detail, name='artefact_detail'),
    url(r'^add/$', add_artefact, name='add_artefact'),
    url(r'^edit/(?P<id>\d+)/$', edit_artefact_detail, name='edit_artefact_detail'),
    url(r'^delete/(?P<pk>\d+)/$', delete_artefact, name='delete_artefact'),
     ]
