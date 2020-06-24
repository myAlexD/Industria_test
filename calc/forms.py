from django import forms
from .models import Currency

CURR_CHOICES = (
    (tuple([i,x]) for i,x in enumerate(Currency.objects.all()))
)

class CurrencyForm(forms.Form):
    currency = forms.ChoiceField(choices = CURR_CHOICES, initial = 'Select currency',)

