from django.test import TestCase
from .forms import BidsForm


class TestBidsForm(TestCase):

    # Test that form cannot be created with incomplete information

    def test_can_create_a_bid_with_just_a_bid(self):
        form = BidsForm({'bid': 1.00})
        self.assertTrue(form.is_valid())

    # Test that form displays error message on missing information

    def test_correct_message_for_missing_bid(self):
        form = BidsForm({'bid': ''})
        self.assertEqual(form.errors['bid'], [u'This field is required.'])
