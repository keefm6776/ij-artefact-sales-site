from django import forms
from .models import Order

# Taken From Code Instiute Course Notes #


class MakePaymentForm(forms.Form):

    MONTH_CHOICES = [(i, i) for i in range(1, 13)]
    YEAR_CHOICES = [(i, i) for i in range(2019, 2037)]

    credit_card_number = forms.CharField(label='Credit card number',
                                         required=False)
    cvv = forms.CharField(label='Security code (CVV)', required=False)
    expiry_month = forms.ChoiceField(label='Month', choices=MONTH_CHOICES,
                                     required=False)
    expiry_year = forms.ChoiceField(label='Year', choices=YEAR_CHOICES,
                                    required=False)
    stripe_id = forms.CharField(widget=forms.HiddenInput)


class OrderForm(forms.ModelForm):

    class Meta:
        model = Order
        fields = (
            'delivery_full_name', 'delivery_phone_number',
            'delivery_street_address1', 'delivery_street_address2',
            'delivery_town_or_city', 'delivery_county',
            'delivery_country', 'delivery_postcode', )
