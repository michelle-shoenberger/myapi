from django import forms
from .models import Drink, Food

class DrinkForm(forms.ModelForm):
    class Meta:
        model = Drink
        fields = ('name', 'price', 'description')

class FoodForm(forms.ModelForm):
    class Meta:
        model = Food
        fields = ('name', 'price', 'description', 'bread')