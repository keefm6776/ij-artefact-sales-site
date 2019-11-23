from django.db import models
from ecommerce import settings

# Create your models here.

class Artefact(models.Model):
    name = models.CharField(max_length=254, default='', blank=False)
    history = models.TextField()
    description = models.TextField()
    century = models.DecimalField(max_digits=3, decimal_places=0, blank=False)

    ERA_CHOICES = (('AD', 'Anno Domini'),
          ('BC', 'Before Christ'),
    )
    era = models.CharField(max_length=2, choices=ERA_CHOICES)
    image = models.ImageField(upload_to='static')
    price = models.DecimalField(max_digits=9, decimal_places=2, blank=False)
    sold = models.BooleanField(default=False)

    def __str__(self):
        return self.name