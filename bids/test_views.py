from django.test import TestCase
from .models import Bids

class TestBidsViews(TestCase):
    def test_make_bid_page(self):
        artefact = Bids(artefact_id=1,bid=3.00)
        artefact.save()

        page = self.client.get("/bid/make_bid/{0}".format(artefact.id))
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "make_bid.html")
    
    def test_get_edit_page_for_artefact_that_does_not_exist(self):
        page = self.client.get("/bid/make_bid/1")
        self.assertEqual(page.status_code, 404)
