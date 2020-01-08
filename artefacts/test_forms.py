from django.test import TestCase
from .forms import ArtefactForm

# Create your tests here.
class TestArtefactForm(TestCase):

# Test that form cannot be created with incomplete information

    def test_cannot_create_an_artefact_with_just_a_name(self):
        form = ArtefactForm({'name': 'The Holy Grail'})
        self.assertFalse(form.is_valid())
    
    def test_cannot_create_an_artefact_with_just_a_description(self):
        form = ArtefactForm({'description': 'It is very very old'})
        self.assertFalse(form.is_valid())

    def test_cannot_create_an_artefact_with_just_its_history(self):
        form = ArtefactForm({'history': 'Once Upon A Time'})
        self.assertFalse(form.is_valid())

    def test_cannot_create_an_artefact_with_just_the_century(self):
        form = ArtefactForm({'century': 3})
        self.assertFalse(form.is_valid())
    
    def test_cannot_create_an_artefact_with_just_the_era(self):
        form = ArtefactForm({'era': 'AD'})
        self.assertFalse(form.is_valid())
    
    def test_cannot_create_an_artefact_with_just_the_price(self):
        form = ArtefactForm({'price': 500.00})
        self.assertFalse(form.is_valid())
    
    def test_cannot_create_an_artefact_with_just_the_sold_tag(self):
        form = ArtefactForm({'sold': False})
        self.assertFalse(form.is_valid())
    
    # Test that the gives the correct error on missing information
    
    def test_correct_message_for_missing_name(self):
        form = ArtefactForm({'name': ''})
        self.assertEqual(form.errors['name'], [u'This field is required.'])
    
    def test_correct_message_for_missing_description(self):
        form = ArtefactForm({'description': ''})
        self.assertEqual(form.errors['description'], [u'This field is required.'])

    def test_correct_message_for_missing_history(self):
        form = ArtefactForm({'history': ''})
        self.assertEqual(form.errors['history'], [u'This field is required.'])
    
    def test_correct_message_for_missing_era(self):
        form = ArtefactForm({'era': ''})
        self.assertEqual(form.errors['era'], [u'This field is required.'])
    
    def test_correct_message_for_missing_price(self):
        form = ArtefactForm({'price': ''})
        self.assertEqual(form.errors['price'], [u'This field is required.'])
    
    def test_correct_message_for_missing_century(self):
        form = ArtefactForm({'century': ''})
        self.assertEqual(form.errors['century'], [u'This field is required.'])

# Test that the gives the correct error on incorrect information
    
   #def test_correct_message_for_price_of_zero(self):
   #     form = ArtefactForm({'price': 0})
   #     self.assertEqual(form.errors['price'], [u'The Price Set Cannot be negative or zero!'])
    
   # def test_correct_message_for_negative_price(self):
   #     form = ArtefactForm({'price': -1})
   #     self.assertEqual(form.errors['price'], [u'The Price Set Cannot be negative or zero!'])
    
   # def test_correct_message_for_century_of_zero(self):
   #     form = ArtefactForm({'century': 0})
   #     self.assertEqual(form.errors['century'], [u'The Century Cannot be negative or zero!'])
    
   # def test_correct_message_for_negative_century(self):
   #     form = ArtefactForm({'century': -1})
   #     self.assertEqual(form.errors['century'], [u'The Century Cannot be negative or zero!'])