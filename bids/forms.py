from django import forms
from .models import Bids


class BidsForm(forms.ModelForm):

    class Meta:
        model = Bids
        fields = ('bid',)
