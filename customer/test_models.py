from django.test import TestCase
from .models import Customer


class CustomerTests(TestCase):
    """ Tests to run against our Customer Models """

    # def test_user_ok(self):
    #   test_user = Customer(user=instance)
    #   self.assertEqual(test_user.user, user=instance)

    def test_full_name_ok(self):
        test_full_name = Customer(full_name='John Doe')
        self.assertEqual(str(test_full_name.full_name), 'John Doe')

    def test_street_Address1_ok(self):
        test_street_Address1 = Customer(street_Address1='Any Street')
        self.assertEqual(str(test_street_Address1.street_Address1),
                         'Any Street')

    def test_street_Address2_ok(self):
        test_street_Address2 = Customer(street_Address2='Any Street')
        self.assertEqual(str(test_street_Address2.street_Address2),
                         'Any Street')

    def test_town_or_city_ok(self):
        test_town_or_city = Customer(town_or_city='Limerick')
        self.assertEqual(str(test_town_or_city.town_or_city), 'Limerick')

    def test_county_ok(self):
        test_county = Customer(county='County Limerick')
        self.assertEqual(str(test_county.county), 'County Limerick')

    def test_country_ok(self):
        test_country = Customer(country='Republic Of Ireland')
        self.assertEqual(str(test_country.country), 'Republic Of Ireland')

    def test_postcode_ok(self):
        test_postcode = Customer(postcode='D14NY88')
        self.assertEqual(str(test_postcode.postcode), 'D14NY88')

    def test_phone_number_ok(self):
        test_phone_number = Customer(phone_number='0871234567')
        self.assertEqual(str(test_phone_number.phone_number), '0871234567')

    def test_email_ok(self):
        test_email = Customer(email='JohnDoe@Any.Com')
        self.assertEqual(str(test_email.email), 'JohnDoe@Any.Com')
