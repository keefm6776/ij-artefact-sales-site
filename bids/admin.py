from django.contrib import admin
from .models import Bids

# Register your models here.

class BidsAdminInline(admin.TabularInline):
    model = Bids

admin.site.register(Bids)