from django.test import TestCase
from .models import Artefact

class ArtefactTests(TestCase):
    """ Tests to run against our Artefact Models """

    def test_name_ok(self):
        test_name = Artefact(name='The Holy Grail')
        self.assertEqual(str(test_name), 'The Holy Grail')

    def test_description_ok(self):
        test_description = Artefact(description='Really Old')
        self.assertEqual(str(test_description.description), 'Really Old')

    def test_history_ok(self):
        test_history = Artefact(history='Made a Long Time Ago!')
        self.assertEqual(str(test_history.history), 'Made a Long Time Ago!')

    def test_century_ok(self):
        test_century = Artefact(century=19)
        self.assertEqual(test_century.century, 19)

    def test_era_ok(self):
        test_era = Artefact(era='AD')
        self.assertEqual(str(test_era.era), 'AD')

    def test_price_ok(self):
        test_price = Artefact(price=13000.00)
        self.assertEqual(test_price.price, 13000)

    def test_sold_ok(self):
        test_sold = Artefact(sold=True)
        self.assertEqual(test_sold.sold, True)