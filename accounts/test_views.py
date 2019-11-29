from django.test import TestCase

class TestAccountsViews(TestCase):

    def test_get_registration_page(self):
        page = self.client.get("/accounts/register/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "register.html")
    