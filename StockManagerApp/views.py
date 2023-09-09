from django.shortcuts import render, redirect

from .forms import StockForm
from .models import Stock


def food_item_list(request):
    food_items = Stock.objects.all()
    return render(request, 'StockManagerApp/food_item_list.html', {'food_items': food_items})


def add_food_item(request):
    if request.method == 'POST':
        form = StockForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('food_item_list')
    else:
        form = StockForm()
    return render(request, 'StockManagerApp/add_food_item.html', {'form': form})


def edit_food_item(request, pk):
    food_item = Stock.objects.get(pk=pk)
    if request.method == 'POST':
        form = StockForm(request.POST, instance=food_item)
        if form.is_valid():
            form.save()
            return redirect('food_item_list')
    else:
        form = StockForm(instance=food_item)
    return render(request, 'StockManagerApp/edit_food_item.html', {'form': form, 'food_item': food_item})


def view_food_item(request, pk):
    food_item = Stock.objects.get(pk=pk)
    return render(request, 'StockManagerApp/view_food_item.html', {'food_item': food_item})

