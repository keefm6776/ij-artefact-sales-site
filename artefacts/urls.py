from django.conf.urls import url
from .views import all_artefacts, artefact_detail, add_artefact, edit_artefact_detail, delete_artefact

urlpatterns = [
    url(r'^$', all_artefacts, name='artefact'),
    url(r'^(?P<pk>\d+)/$', artefact_detail, name='artefact_detail'),
    url(r'^add/$', add_artefact, name='add_artefact'),
    url(r'^edit/(?P<id>\d+)/$', edit_artefact_detail, name='edit_artefact_detail'),
    url(r'^delete/(?P<pk>\d+)/$', delete_artefact, name='delete_artefact'),
     ]
