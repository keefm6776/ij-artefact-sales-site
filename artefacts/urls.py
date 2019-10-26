from django.conf.urls import url
from .views import all_artefacts, artefact_detail, add_artefact

urlpatterns = [
    url(r'^$', all_artefacts, name='artefact'),
    url(r'^(?P<pk>\d+)/$', artefact_detail, name='artefact_detail'),
    url(r'^add/$', add_artefact, name='add_artefact')]
