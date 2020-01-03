from django.db import models
from ecommerce import settings

# Create your models here.


class Artefact(models.Model):
    name = models.CharField(max_length=254, default='', blank=False)
    history = models.TextField(blank=False)
    description = models.TextField(blank=False)
    century = models.DecimalField(max_digits=5, decimal_places=0, blank=False)

    ERA_CHOICES = (
        ('AD', 'Anno Domini'),
        ('BC', 'Before Christ'),
    )
    era = models.CharField(max_length=2, choices=ERA_CHOICES, blank=False)
    image = models.ImageField(upload_to='static', blank=True)
    price = models.DecimalField(max_digits=9, decimal_places=2, blank=False)
    sold = models.BooleanField(default=False)
    despatched = models.BooleanField(default=False)
    despatch_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.name