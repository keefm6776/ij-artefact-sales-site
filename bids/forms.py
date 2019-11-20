from django import forms
from .models import Bids

class BidsForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        my_arg = kwargs.pop('my_arg')
        super(BidsForm, self).__init__(*args, **kwargs)

    class Meta:
        model = Bids
        fields = ('bid',)
       # widgets = {
       #     'bid': forms.NumberInput(attrs={'step': 10.00, 'min_value': {{ my_arg }} }),         
       # }
