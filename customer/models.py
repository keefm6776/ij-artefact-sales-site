from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=60, blank=False)
    street_Address1 = models.CharField(max_length=40, blank=False)
    street_Address2 = models.CharField(max_length=40, blank=False)
    town_or_city = models.CharField(max_length=40, blank=False)
    county = models.CharField(max_length=40, blank=False)
    country = models.CharField(max_length=40, blank=False)
    postcode = models.CharField(max_length=20, blank=False)
    phone_number = models.CharField(max_length=20, blank=False)
    email = models.CharField(max_length=254, blank=False)
    
    def __str__(self):
        return str(self.id)

# Extending User Model with Customer Model adapted from code at Simpleisbetterthancomplex.com

@receiver(post_save, sender=User)
def create_customer_profile(sender, instance, created, **kwargs):
    if created:
       Customer.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_customer_profile(sender, instance, **kwargs):
    instance.customer.save()
