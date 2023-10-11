from .models import Stock, ChefStockResource


def get_context(user_type, pk):
    if user_type == "Storekeeper":
        return Stock.objects.get(pk=pk)
    elif user_type == "Chef":
        return ChefStockResource.objects.get(pk=pk)
