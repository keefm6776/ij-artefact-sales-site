from django.test import TestCase
from .models import Order, OrderLineItem
import datetime


class OrderTests(TestCase):
    """ Tests to run against our Order Models """

    def test_date_ok(self):
        today = datetime.date.today()
        test_date = Order(date=today)
        self.assertEqual(test_date.date, today)

    def test_delivery_full_name_ok(self):
        test_delivery_full_name = Order(delivery_full_name=
                                        'Pippy Longstockings')
        self.assertEqual(str(test_delivery_full_name.delivery_full_name),
                         'Pippy Longstockings')

    def test_delivery_street_address1(self):
        test_delivery_street_address1 = Order(delivery_street_address1=
                                              '12 Any Avenue')
        self.assertEqual(str(test_delivery_street_address1.
                             delivery_street_address1), '12 Any Avenue')

    def test_delivery_street_address2(self):
        test_delivery_street_address2 = Order(delivery_street_address2=
                                              'Any Area')
        self.assertEqual(str(test_delivery_street_address2.
                         delivery_street_address2), 'Any Area')

    def test_delivery_town_or_city_ok(self):
        test_delivery_town_or_city = Order(delivery_town_or_city='Dublin')
        self.assertEqual(test_delivery_town_or_city.
                         delivery_town_or_city, 'Dublin')

    def test_delivery_county(self):
        test_delivery_county = Order(delivery_county='County Dublin')
        self.assertEqual(str(test_delivery_county.
                         delivery_county), 'County Dublin')

    def test_delivery_country(self):
        test_delivery_country = Order(delivery_country='Republic Of Ireland')
        self.assertEqual(str(test_delivery_country.
                         delivery_country), 'Republic Of Ireland')

    def test_delivery_postcode_ok(self):
        test_delivery_postcode = Order(delivery_postcode='D07EV99')
        self.assertEqual(test_delivery_postcode.
                         delivery_postcode, 'D07EV99')

    def test_delivery_phone_number_ok(self):
        test_delivery_phone_number = Order(delivery_phone_number='0871234567')
        self.assertEqual(test_delivery_phone_number.
                         delivery_phone_number, '0871234567')

    def test_delivery_email_ok(self):
        test_delivery_email = Order(delivery_email='JohnDoe@Test.Com')
        self.assertEqual(test_delivery_email.
                         delivery_email, 'JohnDoe@Test.Com')

    # def test_customer_id_ok(self):
    #    test_customer_id = Order(customer_id=Instance)
    #    self.assertEqual(test_customer_id.customer_id, Instance)


class OrderLineItemTests(TestCase):
    """ Tests to run against our OrderLineItem Models """

    # def test_order_id_ok(self):
    #    test_order_id = OrderLineItem(order_id=Instance)
    #    self.assertEqual(test_order_id.order_id, Instance)

    # def test_artefact_id_ok(self):
    #    test_artefact_id = OrderLineItem(artefact_id=Instance)
    #    self.assertEqual(test_artefact_id.artefact_id, Instance)

    def test_quantity_ok(self):
        test_quantity = OrderLineItem(quantity=2)
        self.assertEqual(test_quantity.quantity, 2)

