from django.test import TestCase
from artefacts.models import Artefact


class TestSearchViews(TestCase):

    def test_search_for_sale_artefacts_page(self):

        page = self.client.get("/search/search_for_sale?artefact_name=holy&low_artefact_century=0&high_artefact_century=100&artefact_era=AD")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "artefacts.html")

    def test_search_sold_artefacts_page(self):
        page = self.client.get("/search/search_sold?artefact_name=holy&low_artefact_century=0&high_artefact_century=100&artefact_era=AD")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "artefacts_sold.html")

    def test_search_despatched_artefacts_page(self):
        page = self.client.get("/search/search_despatched?artefact_name=holy&low_artefact_century=0&high_artefact_century=100&artefact_era=AD")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "artefacts_despatched.html")
