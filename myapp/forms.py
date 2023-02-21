from django import forms
from .models import Drink

class DrinkForm(forms.ModelForm):
    class Meta:
        model = Drink
        fields = ('name', 'price', 'description')
