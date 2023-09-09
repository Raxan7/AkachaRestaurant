# forms.py

from django import forms
from .models import Stock


class StockForm(forms.ModelForm):
    class Meta:
        model = Stock
        fields = ['name', 'description', 'quantity', 'expiration_date', 'reorder_quantity']
