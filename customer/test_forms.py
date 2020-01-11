from django.test import TestCase
from .forms import CustomerForm


class TestCustomerForm(TestCase):
    # Test that form cannot be created with incomplete information

    # def test_cannot_process_customer_addition_or_edit_with_just_a_user(self):
    #    form = CustomerForm({'user': instance})
    #    self.assertFalse(form.is_valid())

    def test_cant_process_customer_add_or_edit_with_just_a_full_name(self):
        form = CustomerForm({'full_name': 'pippy longstockings'})
        self.assertFalse(form.is_valid())

    def test_cant_process_customer_add_or_edit_with_just_street_Address1(self):
        form = CustomerForm({'street_Address1': '20 Anywhere Street'})
        self.assertFalse(form.is_valid())

    def test_cant_process_customer_add_or_edit_with_just_street_Address2(self):
        form = CustomerForm({'street_Address2': 'AnyDistrict'})
        self.assertFalse(form.is_valid())

    def test_cant_process_customer_add_or_edit_with_just_town_or_city(self):
        form = CustomerForm({'town_or_city': 'Limerick'})
        self.assertFalse(form.is_valid())

    def test_cant_process_customer_add_or_edit_with_just_a_county(self):
        form = CustomerForm({'county': 'Tipperary'})
        self.assertFalse(form.is_valid())

    def test_cant_process_customer_add_or_edit_with_just_a_country(self):
        form = CustomerForm({'country': 'Republic Of Ireland'})
        self.assertFalse(form.is_valid())

    def test_cant_process_customer_add_or_edit_with_just_a_postcode(self):
        form = CustomerForm({'postcode': 'D07EX90'})
        self.assertFalse(form.is_valid())

    def test_cant_process_customer_add_or_edit_with_just_a_phone_number(self):
        form = CustomerForm({'phone_number': '0871234567'})
        self.assertFalse(form.is_valid())

    def test_cant_process_customer_add_or_edit_with_just_an_email(self):
        form = CustomerForm({'email': 'johndoe@gmail.com'})
        self.assertFalse(form.is_valid())

    # Test that the gives the correct error on missing information

    def test_correct_message_for_full_name(self):
        form = CustomerForm({'form': ''})
        form.is_valid()
        self.assertEqual(form.errors['full_name'],
                         [u'This field is required.'])

    def test_correct_message_for_street_Address1(self):
        form = CustomerForm({'form': ''})
        form.is_valid()
        self.assertEqual(form.errors['street_Address1'],
                         [u'This field is required.'])

    def test_correct_message_for_street_Address2(self):
        form = CustomerForm({'form': ''})
        form.is_valid()
        self.assertEqual(form.errors['street_Address2'],
                         [u'This field is required.'])

    def test_correct_message_for_town_or_city(self):
        form = CustomerForm({'form': ''})
        form.is_valid()
        self.assertEqual(form.errors['town_or_city'],
                         [u'This field is required.'])

    def test_correct_message_for_county(self):
        form = CustomerForm({'form': ''})
        form.is_valid()
        self.assertEqual(form.errors['county'],
                         [u'This field is required.'])

    def test_correct_message_for_country(self):
        form = CustomerForm({'form': ''})
        form.is_valid()
        self.assertEqual(form.errors['country'],
                         [u'This field is required.'])

    def test_correct_message_for_postcode(self):
        form = CustomerForm({'form': ''})
        form.is_valid()
        self.assertEqual(form.errors['postcode'],
                         [u'This field is required.'])

    def test_correct_message_for_phone_number(self):
        form = CustomerForm({'form': ''})
        form.is_valid()
        self.assertEqual(form.errors['phone_number'],
                         [u'This field is required.'])
