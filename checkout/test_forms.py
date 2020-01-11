from django.test import TestCase
from .forms import MakePaymentForm, OrderForm


class TestMakePaymentForm(TestCase):

    # Test that form cannot be created with incomplete information

    def test_cannot_process_payment_with_just_a_card_number(self):
        form = MakePaymentForm({'credit_card_number': '4242424242424242'})
        self.assertFalse(form.is_valid())

    def test_cannot_process_payment_with_just_a_cvv(self):
        form = MakePaymentForm({'cvv': '123'})
        self.assertFalse(form.is_valid())

    def test_cannot_process_payment_with_just_expiry_month(self):
        form = MakePaymentForm({'expiry_month': '12'})
        self.assertFalse(form.is_valid())

    def test_cannot_process_payment_with_just_expiry_year(self):
        form = MakePaymentForm({'expiry_year': '20'})
        self.assertFalse(form.is_valid())

    def test_cannot_process_payment_with_just_stripe_id(self):
        form = MakePaymentForm({'stipe_id': 'AX1009'})
        self.assertFalse(form.is_valid())
