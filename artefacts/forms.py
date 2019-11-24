from django import forms
from .models import Artefact


class ArtefactForm(forms.ModelForm):
    class Meta:
        model = Artefact
        fields = (
            'name', 'description', 'history', 'century',
            'era', 'price', 'sold'
        )
