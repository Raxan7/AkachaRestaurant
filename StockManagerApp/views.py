from django.contrib import messages
from django.shortcuts import render, redirect

# from hotelmanagement.models import Messages
from hotelmanagement.user_validator import user_validator

from .forms import StockForm, PurchasesForm, RequestFoodFromStore, UseFoodItemForm
from .models import Stock, StockPurchases, ChefStockResource
from hotelmanagement.message_handler import send_message
from .helper import get_context


def food_item_list(request):
    food_items = Stock.objects.all()
    return render(request, f'StockManagerApp/{user_validator(request)}/food_item_list.html', {'food_items': food_items})


def add_food_item(request):
    if request.method == 'POST':
        form = StockForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('food_item_list')
    else:
        form = StockForm()
    return render(request, f'StockManagerApp/{user_validator(request)}/add_food_item.html', {'form': form})


def edit_food_item(request, pk):
    food_item = Stock.objects.get(pk=pk)
    if request.method == 'POST':
        form = StockForm(request.POST, instance=food_item)
        if form.is_valid():
            form.save()
            return redirect('food_item_list')
    else:
        form = StockForm(instance=food_item)
    return render(request, f'StockManagerApp/{user_validator(request)}/edit_food_item.html',
                  {'form': form, 'food_item': food_item})


def view_food_item(request, pk):
    food_item = get_context(str(user_validator(request)), pk)
    return render(request, f'StockManagerApp/{user_validator(request)}/view_food_item.html',
                  {'food_item': food_item})


def manage_sales(request):
    return render(request, f'StockManagerApp/{user_validator(request)}/manage_sales.html')


def purchase_registration(request):
    if request.method == "POST":
        form = PurchasesForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.recorder = request.user
            instance.save()
            return redirect('purchases_list')
    else:
        form = PurchasesForm()
    return render(request, f'StockManagerApp/{user_validator(request)}/purchase_register.html',
                  {'form': form})


def purchases_list_view(request):
    objs = StockPurchases.objects.all()
    return render(request, f'StockManagerApp/{user_validator(request)}/purchase_list.html',
                  {"objs": objs})


def purchases_detail(request, pk):
    obj = StockPurchases.objects.get(id=pk)
    return render(request, f'StockManagerApp/{user_validator(request)}/purchases_detail_view.html',
                  {"obj": obj})


def request_food_items_view(request):

    # display messages
    system_sms = Messages.objects.all().order_by('-time_sent')
    # Request food item from Store
    if request.method == 'POST':
        form = RequestFoodFromStore(request.POST)
        if form.is_valid():
            name_request = request.POST.get("name")
            quantity_request = request.POST.get('quantity')

            stock_object = Stock.objects.get(pk=name_request)
            is_authorized = False
            if int(quantity_request) > stock_object.quantity:
                messages.error(request,
                               f"The amount of {stock_object.name} available is {stock_object.quantity} units",
                               fail_silently=True)
            else:
                stock_object.quantity = stock_object.quantity - int(quantity_request)
                is_authorized = True
                stock_object.save()

            if is_authorized:
                if ChefStockResource.objects.get(pk=name_request):
                    chef_model = ChefStockResource.objects.get(pk=name_request)
                    chef_model.quantity = chef_model.quantity + int(quantity_request)
                else:
                    chef_model = ChefStockResource.objects.create(
                        name=stock_object.name,
                        description=stock_object.description,
                        quantity=int(quantity_request),
                        expiration_date=stock_object.expiration_date,
                        reorder_quantity=(3 / 4 * int(quantity_request))
                    )
                chef_model.save()
                message = (f"{str(request.user.user_type)} {request.user.first_name} {request.user.first_name}"
                           f" has taken {quantity_request} unit of {stock_object.name} from Store")
                send_message(request.user, str(request.user.user_type),
                             message, "Request")
            form.save()
            return redirect('food_item_list')
    else:
        form = RequestFoodFromStore()
    return render(request, f'StockManagerApp/{user_validator(request)}/request_food_item.html',
                  {'form': form, 'system_sms': system_sms})


def use_food_item(request):
    # display messages
    system_sms = Messages.objects.all().order_by('-time_sent')
    # Request food item from Store
    if request.method == 'POST':
        form = UseFoodItemForm(request.POST)
        if form.is_valid():
            name_request = request.POST.get("name")
            quantity_request = request.POST.get('quantity')

            stock_object = Stock.objects.get(pk=name_request)
            is_authorized = False
            if int(quantity_request) > stock_object.quantity:
                messages.error(request,
                               f"The amount of {stock_object.name} available is {stock_object.quantity} units",
                               fail_silently=True)
            else:
                stock_object.quantity = stock_object.quantity - int(quantity_request)
                is_authorized = True
                stock_object.save()

            if is_authorized:
                if ChefStockResource.objects.get(pk=name_request):
                    chef_model = ChefStockResource.objects.get(pk=name_request)
                    chef_model.quantity = chef_model.quantity + int(quantity_request)
                else:
                    chef_model = ChefStockResource.objects.create(
                        name=stock_object.name,
                        description=stock_object.description,
                        quantity=int(quantity_request),
                        expiration_date=stock_object.expiration_date,
                        reorder_quantity=(3 / 4 * int(quantity_request))
                    )
                chef_model.save()
                message = (f"{str(request.user.user_type)} {request.user.first_name} {request.user.first_name}"
                           f" has taken {quantity_request} unit of {stock_object.name} from Store")
                send_message(request.user, str(request.user.user_type),
                             message, "Request")
            form.save()
            return redirect('food_item_list')
    else:
        form = UseFoodItemForm()
    return render(request, f'StockManagerApp/{user_validator(request)}/request_food_item.html',
                  {'form': form, 'system_sms': system_sms})
