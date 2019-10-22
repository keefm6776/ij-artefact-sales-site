from django.conf.urls import url, include
from django.contrib import admin
from django.views.generic import RedirectView
from django.views.static import serve
from .views import all_artefacts, artefact_detail

urlpatterns = [
    url(r'^$', all_artefacts, name='artefact'),
    url(r'^(?P<pk>\d+)/$', artefact_detail, name='artefact_detail'),
]