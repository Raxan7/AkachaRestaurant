import StockManagerApp.models
from .models import Stock, ChefStockResource
from django.shortcuts import redirect


def get_context(user_type, name):
    if user_type == "Storekeeper":
        return Stock.objects.get(name=name)
    elif user_type == "Chef":
        try:
            return ChefStockResource.objects.get(name=name)
        except Exception as e:
            return redirect("home")
