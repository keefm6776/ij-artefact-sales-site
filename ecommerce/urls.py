"""ecommerce URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from accounts import urls as urls_accounts
from artefacts import urls as urls_artefacts
from cart import urls as urls_cart
from artefacts.views import all_artefacts
from django.views import static
from .settings import MEDIA_URL

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url('r^$', all_artefacts, name='index'),
    url(r'^accounts/', include(urls_accounts)),
    url(r'^artefacts/', include(urls_artefacts)),
    url(r'^cart/', include(urls_cart)),
    url(r'^media/(?P<path>.*)$', static.serve, {'document_root': MEDIA_URL}),
]
