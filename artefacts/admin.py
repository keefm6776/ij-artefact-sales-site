from django.contrib import admin
from .models import Artefact

# Register your models here.

from django.contrib import admin
from artefacts.models import Artefact
from customer.models import Customer


# Register your models here.

admin.site.register(Artefact)
admin.site.register(Customer)

