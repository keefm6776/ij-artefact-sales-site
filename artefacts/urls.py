from django.conf.urls import url
from .views import all_artefacts, artefact_detail

urlpatterns = [
    url(r'^$', all_artefacts, name='artefact'),
    url(r'^(?P<pk>\d+)/$', artefact_detail, name='artefact_detail')]
