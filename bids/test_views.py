from django.test import TestCase, Client
from django.contrib.auth.models import User
from .models import Bids
from artefacts.models import Artefact
from customer.models import Customer
from customer.forms import CustomerForm
from accounts.forms import UserRegistrationForm

class TestBidsViews(TestCase):#
#
#    Unable to create user instance to get this to run
#
#    def test_make_bid_page(self):   #
#
#
 #       artefact = Artefact(name="The Holy Grail", century=3, price=3.00, history="It happened a long time ago",
#                        description="It is really old", era="AD", sold=False, despatched=False)
#        artefact.save()
#
#        customer = Customer(full_name="Pippy Longstockings", user=user_instance, street_Address1="10 Any Street", street_Address2="Any Area",
#                            town_or_city="Dublin", county="Dublin", country="Ireland", postcode="D01EO90", phone_number="0871234567")
#        customer.save()
#    
#        page = self.client.get("/bid/make_bid/{0}/".format(artefact.id))
#        self.assertEqual(page.status_code, 200)
#        self.assertTemplateUsed(page, "make_bid.html")
    
    def test_get_edit_page_for_artefact_that_does_not_exist(self):
        page = self.client.get("/bid/make_bid/1")
        self.assertEqual(page.status_code, 404)
