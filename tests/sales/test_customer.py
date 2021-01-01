from django.test import TestCase
from sales.models import Customer, CustomerContact


class CustomerTestCase(TestCase):
    def setUp(self):
        Customer.objects.create(
            name="customer 1", address="test address", postcode="test"
        )
        self.customer = Customer.objects.get(name="customer 1")
        CustomerContact.objects.create(
            customer=self.customer, first_name="Hello", last_name="World!"
        )
        self.customer_contact = CustomerContact.objects.get(customer=self.customer)

    def test_customer(self):
        self.assertEqual(self.customer.__str__(), "customer 1")

    def test_customer_contact(self):
        self.assertEqual(self.customer_contact.__str__(), "Hello World!")
