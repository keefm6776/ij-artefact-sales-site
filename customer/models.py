from django.db import models

class Customer(models.Model):
    full_name = models.CharField(max_length=60, default='')
    street_Address1 = models.CharField(max_length=40, default='')
    street_Address2 = models.CharField(max_length=40, default='')
    town_or_city = models.CharField(max_length=40, default='')
    county = models.CharField(max_length=40, default='')
    country = models.CharField(max_length=40, default='')
    postcode = models.CharField(max_length=20, default='')
    phone_number = models.CharField(max_length=20, default='')
    email = models.CharField(max_length=254, default='')

    def __str__(self):
        return self.name
