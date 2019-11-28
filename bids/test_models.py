from django.test import TestCase
from .models import Bids

class BidsTests(TestCase):
    """ Tests to run against our Bids Models """

   # def test_artefact_id_ok(self):
    #    test_artefact_id = Bids(artefact_id={id:8, name:'Holy Grail'})
     #   self.assertEqual(test_artefact_id.artefact_id, artefact_id={id:8, name:'Holy Grail'})

    #def test_customer_id_ok(self):
    #    test_customer_id = Bids(customer_id=34)
    #    self.assertEqual(test_artefact_id.artefact_id, 34)

    def test_bid_ok(self):
        test_bid = Bids(bid=22.00)
        self.assertEqual(test_bid.bid, 22.00)

    def test_date_ok(self):
        test_date = Bids(date='06/07/1976')
        self.assertEqual(test_date.date, '06/07/1976')

        