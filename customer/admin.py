from django.contrib import admin
from .models import Customer

# Register your models here.


class CustomerAdminInline(admin.TabularInline):
    model = Customer

admin.site.register(Customer)