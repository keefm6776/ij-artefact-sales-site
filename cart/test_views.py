from django.test import TestCase
from artefacts.models import Artefact


class TestCartViews(TestCase):
    # def test_view_cart_page(self):
    #    page = self.client.get("/cart/")
    #    self.assertEqual(page.status_code, 302) #Redirect

    def test_add_to_cart_page(self):
        artefact = Artefact(name="The Holy Grail", century=3, price=3.00)
        artefact.save()

        page = self.client.get("/cart/add/{0}/".format(artefact.id))
        self.assertEqual(page.status_code, 302)  # Redirect

    # def test_adjust_cart_page(self):
    #    artefact = Artefact(name="The Holy Grail",century=3,price=3.00)
    #    artefact.save()
    #    page = self.client.get("/cart/adjust/{0}/".format(artefact.id))
    #    self.assertEqual(page.status_code, 200)
