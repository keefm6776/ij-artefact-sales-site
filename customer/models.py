from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Customer(models.Model):
    user = models.OneToOneField(User, related_name='customer',on_delete=models.CASCADE)
    full_name = models.CharField(max_length=60, default='')
    street_Address1 = models.CharField(max_length=40, default='')
    street_Address2 = models.CharField(max_length=40, default='')
    town_or_city = models.CharField(max_length=40, default='')
    county = models.CharField(max_length=40, default='')
    country = models.CharField(max_length=40, default='')
    postcode = models.CharField(max_length=20, default='')
    phone_number = models.CharField(max_length=20, default='')
    email = models.CharField(max_length=254, default='')
    objects=models.Manager()

    def __str__(self):
        return self.user.email

@receiver(post_save, sender=User)
def create_customer_profile(sender, instance, created, **kwargs):
    if created:
       Customer.objects.create(user=instance).save()

@receiver(post_save, sender=User)
def save_customer_profile(sender, instance, **kwargs):
    instance.customer.save()
