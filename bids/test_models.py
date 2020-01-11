from django.test import TestCase
from .models import Bids, Artefact


class BidsTests(TestCase):
    """ Tests to run against our Bids Models """

    # def test_artefact_id_ok(self):
    #    artefact = Artefact(name="The Holy Grail")
    #    artefact.save()
    #    self.assertEqual(artefact.artefact_id,
    #                     artefact_id={name:'Holy Grail'})

    # def test_customer_id_ok(self):
    #    customer = Customer(full_name="Keith Morton")
    #    self.assertEqual(customer.customer_id,
    #                     customer_id={full_name="Keith Morton")

    def test_bid_ok(self):
        test_bid = Bids(bid=22.00)
        self.assertEqual(test_bid.bid, 22.00)

    def test_date_ok(self):
        test_date = Bids(date='06/07/1976')
        self.assertEqual(test_date.date, '06/07/1976')
