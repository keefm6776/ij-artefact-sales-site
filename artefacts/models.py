from django.db import models
from ecommerce import settings

# Create your models here.


class Artefact(models.Model):
    name = models.CharField(max_length=254, default='', blank=True)
    history = models.TextField(blank=True)
    description = models.TextField(blank=True)
    century = models.DecimalField(max_digits=5, decimal_places=0, blank=True)

    ERA_CHOICES = (
        ('AD', 'Anno Domini'),
        ('BC', 'Before Christ'),
    )
    era = models.CharField(max_length=2, choices=ERA_CHOICES, blank=True)
    image = models.ImageField(upload_to='static', blank=True, null=True)
    price = models.DecimalField(max_digits=9, decimal_places=2)
    sold = models.BooleanField(default=False)
    despatched = models.BooleanField(default=False)
    despatch_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.name