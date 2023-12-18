# This form allows selection of multiple burgers, sides, drinks, and sauces.
# python

from django import forms
from .models import Burger, Side, Drink, Sauce


class OrderForm(forms.Form):
    burgers = forms.ModelMultipleChoiceField(
        queryset=Burger.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False,
    )
    sides = forms.ModelMultipleChoiceField(
        queryset=Side.objects.all(), widget=forms.CheckboxSelectMultiple, required=False
    )
    drinks = forms.ModelMultipleChoiceField(
        queryset=Drink.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False,
    )
    sauces = forms.ModelMultipleChoiceField(
        queryset=Sauce.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False,
    )
