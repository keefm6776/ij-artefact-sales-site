from django.contrib import admin
from .models import Bids


class BidsAdminInline(admin.TabularInline):
    model = Bids

admin.site.register(Bids)
