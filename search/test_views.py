#from django.test import TestCase
#from artefacts.models import Artefact

#class TestSearchViews(TestCase):

    #def test_search_for_sale_artefacts_page(self):
    #    artefacts = {"name":'The Holy Grail',
    #                 "century":3,
    #                 "price":3.00,
    #                 "history":'A long long time ago',
    #                 "description":'Really old',
    #                 "era":'AD',
    #                 "sold":False,
    #                 "despatched":False}
        
    #    page = self.client.get("/search/search_for_sale/")
    #    self.assertEqual(page.status_code, 200)
    #    self.assertTemplateUsed(page, "artefacts.html", {"artefacts": artefacts})

    #def test_search_sold_artefacts_page(self):
    #    page = self.client.get("/search/search_sold/")
    #    self.assertEqual(page.status_code, 200)
    #    self.assertTemplateUsed(page, "artefacts_sold.html")

    #def test_search_despatched_artefacts_page(self):
    #    page = self.client.get("/search/search_despatched/")
    #    self.assertEqual(page.status_code, 200)
    #    self.assertTemplateUsed(page, "artefacts_despatched.html")



