from django.test import TestCase
from .models import Artefact


class TestArtefactViews(TestCase):

    def test_get_home_page(self):
        page = self.client.get("/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "base.html")

    def test_get_for_sale_artefacts_page(self):
        page = self.client.get("/artefacts/for_sale/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "artefacts.html")
        
    def test_get_add_artefact_page(self):
        page = self.client.get("/artefacts/add/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "add_artefact.html")
    
    def test_get_sold_artefacts_page(self):
        page = self.client.get("/artefacts/sold/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "artefacts_sold.html")
    
    def test_get_despatched_artefacts_page(self):
        page = self.client.get("/artefacts/despatched/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "artefacts_despatched.html")
    
    #def test_get_edit_artefact_page(self):
     #   artefact = Artefact(name="The Holy Grail",century=3,price=3.00)
      #  artefact.save()

       # page = self.client.get("/artefacts/edit/{0}".format(artefact.id))
        #self.assertEqual(page.status_code, 200)
        #self.assertTemplateUsed(page, "edit_artefact_detail.html")
    
    def test_get_edit_page_for_artefact_that_does_not_exist(self):
        page = self.client.get("/edit/1")
        self.assertEqual(page.status_code, 404)

    #def test_get_delete_artefact_page(self):
     #   artefact = Artefact(name="The Holy Grail",century=3,price=3.00)
      #  artefact.save()

       # page = self.client.get("/artefacts/delete/{0}".format(artefact.id))
        #self.assertRedirects(page, status_code=302, target_status_code=200, msg_prefix='', fetch_redirect_response=True)
        #self.assertEqual(page.status_code, 200)
        #(response, expected_url, status_code=302, target_status_code=200, msg_prefix='', fetch_redirect_response=True)
        #self.assertTemplateUsed(page, "artefacts.html")
    
    def test_get_delete_page_for_artefact_that_does_not_exist(self):
        page = self.client.get("/delete/1")
        self.assertEqual(page.status_code, 404)

    def test_get_despatched_artefact_page(self):
        page = self.client.get("/artefacts/despatched/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "artefacts_despatched.html")

    #def test_get_artefact_detail_page(self):
    #    artefact = Artefact(name="The Holy Grail",century=3,price=3.00)
    #    artefact.save()

    #   page = self.client.get("/artefacts/detail/{0}".format(artefact.id))
    #   self.assertEqual(page.status_code, 200)
    #   self.assertTemplateUsed(page, "artefact_detail.html")
    
    def test_get_artefact_detail_page_for_artefact_that_does_not_exist(self):
        page = self.client.get("/artefacts/1")
        self.assertEqual(page.status_code, 404)