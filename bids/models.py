from django.db import models
from django.utils import timezone
from artefacts.models import Artefact
from customer.models import Customer

class Bids(models.Model):

    artefact_id = models.ForeignKey(Artefact, null=False, default='')
    customer_id = models.ForeignKey(Customer, null=False, default='')
    bid = models.FloatField(null=True, default=0.00)
    date = models.DateTimeField(auto_now_add = True)
        
    def __str__(self):
        return str(self.bid)