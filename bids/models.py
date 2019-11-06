from django.db import models
from artefacts.models import Artefact
from customer.models import Customer

# Create your models here.

class Bids(models.Model):

    artefact_id = models.ForeignKey(Artefact, null=False, default='')
    customer_id = models.ForeignKey(Customer, null=False, default='')
    bid = models.DecimalField(max_digits=6, decimal_places=2, blank=False, default=0.00)
    date = models.DateField()

    def __str__(self):
        return self.bid