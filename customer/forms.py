from django import forms
from customer.models import Customer


class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ('full_name', 'street_Address1', 'street_Address2',
                  'town_or_city', 'county', 'country', 'postcode',
                  'phone_number')
