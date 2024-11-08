# forms.py

from django import forms
from .models import Stock, StockPurchases, RequestStock, UseChefResources


class StockForm(forms.ModelForm):
    class Meta:
        model = Stock
        fields = ['name', 'description', 'quantity', 'expiration_date', 'reorder_quantity']


class PurchasesForm(forms.ModelForm):
    class Meta:
        model = StockPurchases
        fields = ['seller_name', 'goods_bought', 'price', ]


class RequestFoodFromStore(forms.ModelForm):
    quantity = forms.IntegerField(required=True)

    class Meta:
        model = RequestStock
        fields = ['name']


class UseFoodItemForm(forms.ModelForm):
    quantity = forms.IntegerField(required=True)

    class Meta:
        model = UseChefResources
        fields = ['name']
