from django.contrib import messages
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode

from EmailApp.token import account_activation_token
from .EmailBackEnd import EmailBackEnd
from django.contrib.auth import login, logout
from .models import *
from .utils import user_validator
from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Avg
import datetime
from django.contrib.auth import update_session_auth_hash
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import check_password
# from django.views.decorators.cache import cache_page


def check_username_availability(request):
    username = request.GET.get('username')
    exists = CustomUser.objects.filter(username=username).exists()
    return JsonResponse({'exists': exists})


def check_email_availability(request):
    email = request.GET.get('email')
    exists = CustomUser.objects.filter(email=email).exists()
    return JsonResponse({'exists': exists})


# def logins(request):
#     #if request.user.is_authenticated:
#         #return render(request, f"{user_validator(request)}/home.html")
#     if request.method == "POST":
#         username = request.POST.get('email')
#         password = request.POST.get('password')
#         user = EmailBackEnd.authenticate(request, username, password)
#         if user != None:
#             login(request, user)
#             return render(request, f"{user_validator(request)}/home.html")
#         else:
#             messages.error(request, "Invalid credentials!.")
#     return render(request, "login.html")

def logins(request):
    if request.method == "POST":
        username = request.POST.get('email')
        password = request.POST.get('password')
        user = CustomUser.objects.filter(models.Q(username=username) | models.Q(email=username)).first()
        if user and check_password(password, user.password) and user.is_active:
            login(request, user)
            return redirect('home')
        elif not user.is_active:
            messages.error(request, "Verify Your Email First To Login!")
        else:
            messages.error(request, "Invalid Login Credentials!")
            return render(request, 'login.html')
    else:
        return render(request, "login.html")


def index(request):
    return render(request, "index.html")


# @cache_page(60 * 2500)
def home(request):
    return render(request, f"{user_validator(request)}/home.html")


def userprofile(request):
    if request.method == "POST":
        id = int(request.POST.get('id'))
        user = CustomUser.objects.get(id=id)
        base_template = f'{request.user.user_type}/base.html'
        return render(request, 'user_details.html', {'base_template': base_template, 'userr': user})
    return redirect('home')


def logout_user(request):
    logout(request)
    return redirect("index")


def add_user_type(request):
    if request.method == "POST":
        user_type = request.POST.get('user_type')
        User_type.objects.create(user_type=user_type)
        return redirect('home')
    return render(request, f"{user_validator(request)}/add_user_type.html")


def register(request):
    if request.method == "POST":
        first_name = request.POST.get("firstname")
        last_name = request.POST.get("lastname")
        email = request.POST.get("email")
        password = request.POST.get("password")
        password1 = request.POST.get("password1")
        user_type = User_type.objects.get(id=5)
        fullname = first_name + last_name
        email_user_name = f"{first_name} {last_name}"
        if CustomUser.objects.filter(username=fullname).exists():
            fullname = email
        if password != password1:
            messages.error(request, 'Password do not match')
            return render(request, "register.html")
        if CustomUser.objects.filter(email=email).exists():
            messages.error(request, 'Email Already Exists')
            return render(request, "register.html")
        user = CustomUser.objects.create_user(user_type=user_type, username=fullname, email=email, password=password,
                                              first_name=first_name, last_name=last_name, )
        user.is_active = False
        user.save()
        # Get the domain name of the current site
        current_site = get_current_site(request)
        mail_subject = 'Activation link has been sent to your email id'
        message = render_to_string('acc_active_email.html', {
            'user': user,
            'domain': current_site.domain,
            'uid': urlsafe_base64_encode(force_bytes(user.pk)),
            'token': account_activation_token.make_token(user),
        })
        to_email = email
        email = EmailMessage(
            subject=mail_subject,
            body=message,
            from_email="no-reply-akacha@raxan7.com",
            to=[to_email]
        )
        email.send()

        return redirect("verify_email")
    else:
        return render(request, "register.html")


def verify_email(request):
    return render(request, "verify_email.html")


def password_change(request):
    if request.method == 'POST':
        current_password = request.POST['current_password']
        new_password = request.POST['new_password']
        confirm_password = request.POST['confirm_password']
        user = request.user

        if user.check_password(current_password):
            if new_password == confirm_password:
                user.set_password(new_password)
                user.save()
                update_session_auth_hash(request, user)  # Update the user's session
                messages.success(request, 'Password changed successfully.')
                return redirect('profile')  # Redirect to the user's profile page
            else:
                messages.error(request, 'New passwords do not match.')
        else:
            messages.error(request, 'Current password is incorrect.')
    base_template = f'{request.user.user_type}/base.html'

    return render(request, 'password_change.html', {'base_template': base_template})


def delete_user(request, id):
    user = CustomUser.objects.get(id=id)
    user.delete()
    url = request.META.get('HTTP_REFERER')
    return redirect(url)


# 0 means all user types present
def activate_all_user(request):
    users = CustomUser.objects.all()
    for user in users:
        user.is_active = True
        user.save()
    url = request.META.get('HTTP_REFERER')
    return redirect(url)

    # 0 means all user types present


def deactivate_all_user(request):
    users = CustomUser.objects.exclude(user_type=1)
    for user in users:
        if user.user_type != "CEO":
            user.is_active = False
            user.save()
    url = request.META.get('HTTP_REFERER')
    return redirect(url)


def deactivate_user(request, id):
    user = CustomUser.objects.get(id=id)
    if user.user_type != "CEO":
        user.is_active = False
        user.save()
    user.save()
    user_type = user.user_type
    user_types = User_type.objects.get(user_type=user_type)
    type_id = user_types.id
    url = request.META.get('HTTP_REFERER')
    return redirect(url)


def activate_user(request, id):
    user = CustomUser.objects.get(id=id)
    user.is_active = True
    user.save()
    user_type = user.user_type
    user_types = User_type.objects.get(user_type=user_type)
    type_id = user_types.id
    url = request.META.get('HTTP_REFERER')
    return redirect(url)


def add_user(request):
    if request.method == "POST":
        first_name = request.POST.get("firstname")
        last_name = request.POST.get("lastname")
        email = request.POST.get("email")
        user_types = request.POST.get("user_type")
        user_type = User_type.objects.get(id=user_types)
        password = "12345678"
        fullname = first_name + last_name
        url = request.META.get('HTTP_REFERER')
        if CustomUser.objects.filter(username=fullname).exists():
            fullname = email
        if CustomUser.objects.filter(email=email).exists():
            messages.error(request, 'Email Alredy Exists')
            return redirect(url)
        user = CustomUser.objects.create_user(user_type=user_type, username=fullname, email=email, password=password,
                                              first_name=first_name, last_name=last_name, )
        user.save()
        return redirect(url)
    return redirect('manage_user', user_type.id)


def manage_user(request, id):
    if id == 0:
        users = CustomUser.objects.all()
    else:
        users = CustomUser.objects.filter(user_type=id)
    return render(request, f"{user_validator(request)}/manage_user.html", {'users': users})


def edit_user(request):
    if request.method == "POST":
        first_name = request.POST.get("firstname")
        last_name = request.POST.get("lastname")
        email = request.POST.get("email")
        username = request.POST.get("username")
        user_types = request.POST.get("user_type")
        profile = request.FILES.get("image")
        id = request.POST.get("id")
        user_type = User_type.objects.get(id=user_types)
        user = CustomUser.objects.get(id=id)
        user.first_name = first_name
        user.last_name = last_name
        user.email = email
        user.username = username
        user.user_type = user_type
        if profile:
            user.profile = profile
        user.save()
    return redirect('userprofile')


def add_menu_category(request):
    if request.method == "POST":
        name = request.POST['menu_name']
        MenuCategory.objects.create(name=name)
        return redirect("manage_menu_category")


def manage_menu_category(request):
    menus = MenuCategory.objects.all()
    return render(request, f"{user_validator(request)}/manage_menu.html", {"menus": menus})


def edit_menu_category(request, id):
    if request.method == "POST":
        name = request.POST['menu_name']
        menu = MenuCategory.objects.get(id=id)
        menu.name = name
        menu.save()
        return redirect("manage_menu_category")
    menu = MenuCategory.objects.get(id=id)
    return render(request, f"{user_validator(request)}/edit_menu_category.html", {"menu": menu})


def delete_menu_category(request, id):
    menu_category = MenuCategory.objects.get(id=id)
    menu_category.delete()
    return redirect('manage_menu_category')


def add_menu_item(request):
    if request.method == "POST":
        category_id = request.POST["category_id"]
        name = request.POST['item_name']
        description = request.POST['description']
        price = float(request.POST['price'])
        category = MenuCategory.objects.get(id=category_id)
        MenuItem.objects.create(name=name, description=description, price=price, category=category)
        return redirect("manage_menu_item")


def edit_menu_item(request, id):
    if request.method == "POST":
        menuItem = MenuItem.objects.get(id=id)
        category_id = request.POST["category_id"]
        name = request.POST['item_name']
        description = request.POST['description']
        price = request.POST['price']
        category = MenuCategory.objects.get(id=category_id)
        menuItem.name = name
        menuItem.description = description
        menuItem.price = price
        menuItem.category = category
        menuItem.save()
    return redirect("manage_menu_item")


def delete_menu_item(request, id):
    menu_item = MenuItem.objects.get(id=id)
    menu_item.delete()
    return redirect('manage_menu_item')


def manage_menu_item(request):
    menuItems = MenuItem.objects.all().order_by('-name')
    menu_items = []
    for menuitem in menuItems:
        primary_image = MenuImage.objects.filter(menu_item=menuitem).first()
        menu_items.append({
            'menuitems': menuitem,
            'menuimage': primary_image
        })
    categories = MenuCategory.objects.all()
    tables = Table.objects.all()
    return render(request, f"{user_validator(request)}/manage_menu_item.html",
                  {'menu_items': menu_items, 'tables': tables, 'menucategories': categories})


from .models import MenuItem, MenuImage


def menu_items_api(request):
    order = request.GET.get('order_by')
    menu_items = MenuItem.objects.all().order_by(f'{order}')
    menu_items_data = []
    for menu_item in menu_items:
        primary_image = MenuImage.objects.filter(menu_item=menu_item).first()
        menu_items_data.append({
            'id': menu_item.id,
            'name': menu_item.name,
            'price': menu_item.price,
            'image_url': primary_image.image.url if primary_image else None,
            'category': menu_item.category.name,
            'ingredient_cost': menu_item.ingredient_cost,
            'item_profit': menu_item.item_profit,
            'average_rating': menu_item.average_rating,
            'orders_number': menu_item.orders_number,
            # Add other fields as needed
        })
    return JsonResponse({'menu_items': menu_items_data})


def search_menu_items(request):
    query = request.GET.get('query')
    menu_items = MenuItem.objects.filter(name__icontains=query) | MenuItem.objects.filter(
        category__name__icontains=query)
    menu_items_data = []
    for menu_item in menu_items:
        primary_image = MenuImage.objects.filter(menu_item=menu_item).first()
        menu_items_data.append({
            'id': menu_item.id,
            'name': menu_item.name,
            'price': menu_item.price,
            'image_url': primary_image.image.url if primary_image else None,
            'category': menu_item.category.name,
            'ingredient_cost': menu_item.ingredient_cost,
            'item_profit': menu_item.item_profit,
            'average_rating': menu_item.average_rating,
            'orders_number': menu_item.orders_number,
            # Add other fields as needed
        })
    return JsonResponse({'menu_items': menu_items_data})


def filter_menu_item(request, id):
    menu_category = MenuCategory.objects.get(id=id)
    menuItems = MenuItem.objects.filter(category=menu_category).order_by('-name')
    menu_items = []
    for menuitem in menuItems:
        menuitem.profit = menuitem.price - menuitem.cost
        primary_image = MenuImage.objects.filter(menu_item=menuitem).first()
        menu_items.append({
            'menuitems': menuitem,
            'menuimage': primary_image
        })
    tables = Table.objects.all()
    return render(request, f"{user_validator(request)}/manage_menu_item.html",
                  {'menu_items': menu_items, 'tables': tables})


def menu_item_description(request, item_id):
    rating_data = MenuItemRating.objects.filter(menu_item__id=item_id)
    ratings = rating_data.values('rating').annotate(count=models.Count('rating'),
                                                    percent=models.Count('rating') * 100 / (
                                                        rating_data.count())).order_by('rating')
    menuitem = MenuItem.objects.get(id=item_id)
    images = MenuImage.objects.filter(menu_item=menuitem)
    return render(request, f"{user_validator(request)}/menu_description.html",
                  {'images': images, 'menuitem': menuitem, 'ratings': ratings, 'rating_data': rating_data})


def rate_menu_item_ajax(request, menu_item_id):
    if request.method == 'POST':
        comment = request.POST['comment']
        menu_item = get_object_or_404(MenuItem, pk=menu_item_id)
        has_rated = MenuItemRating.objects.filter(user=request.user, menu_item=menu_item).exists()

        if not has_rated:
            rating = int(request.POST.get('rating'))
            menu_item_rating = MenuItemRating(user=request.user, menu_item=menu_item, rating=rating, comment=comment)
            menu_item_rating.save()

            # Calculate and update the average rating for the menu item
            menu_item.average_rating = MenuItemRating.objects.filter(menu_item=menu_item).aggregate(Avg('rating'))[
                'rating__avg']
            menu_item.save()
            messages.success(request, "Rating Submitted successfully")
        else:
            messages.error(request, "You have alredy rated this food menu item")
    return redirect('my_order')


def add_menu_image(request):
    if request.method == "POST":
        menu_id = request.POST['menu_id']
        image = request.FILES.get('image')
        menu = MenuItem.objects.get(id=menu_id)
        MenuImage.objects.create(menu_item=menu, image=image)
        return redirect("manage_menu_image")


def manage_menu_image(request):
    menu_images = MenuImage.objects.all()
    menuitems = MenuItem.objects.all()
    return render(request, f"{user_validator(request)}/manage_menu_image.html",
                  {'images': menu_images, 'menuitems': menuitems})


def edit_menu_image(request, id):
    if request.method == "POST":
        menu_id = int(request.POST.get('menu_id'))
        image = request.FILES.get('image')
        menu = MenuItem.objects.get(id=menu_id)
        menu_image = MenuImage.objects.get(id=id)
        if image:
            menu_image.image = image
        menu_image.menu_item = menu
        menu_image.save()
    return redirect("manage_menu_image")


def delete_menu_image(request, id):
    menu_image = MenuImage.objects.get(id=id)
    menu_image.delete()
    return redirect("manage_menu_image")


def add_restaurant(request):
    if request.method == "POST":
        name = request.POST['name']
        location = request.POST['location']
        description = request.POST['description']
        contact = request.POST['contact']
        Restaurant.objects.create(name=name, location=location, description=description, contact=contact)
    return render(request, f"{user_validator(request)}/add_restaurant.html")


def manage_restaurant(request):
    restaurants = Restaurant.objects.all()
    return render(request, f"{user_validator(request)}/manage_restaurant.html", {"restaurants": restaurants})


def edit_restaurant(request, id):
    if request.method == "POST":
        restaurant = Restaurant.objects.get(id=id)
        name = request.POST['name']
        location = request.POST['location']
        description = request.POST['description']
        contact = request.POST['contact']
        restaurant.name = name
        restaurant.location = location
        restaurant.description = description
        restaurant.contact = contact
        restaurant.save()
        return redirect("/")
    restaurant = Restaurant.objects.get(id=id)
    return render(request, f"{user_validator(request)}/edit_restaurant.html", {"restaurant": restaurant})


def add_table(request):
    if request.method == "POST":
        table_number = request.POST["table_number"]
        # restaurant_id = request.POST["restaurant_id"]
        capacity = request.POST["table_capacity"]
        # restaurant = Restaurant.objects.get(id = restaurant_id)
        Table.objects.create(table_number=table_number, capacity=capacity)
    return redirect("manage_table")


def manage_table(request):
    tables = Table.objects.all()
    return render(request, f"{user_validator(request)}/manage_table.html", {'tables': tables})


def add_order(request):
    if request.method == "POST":
        table_id = request.POST.get('table_id')
        menu_id = request.POST.get('menu_id')
        latitude = request.POST.get('latitude')
        longitude = request.POST.get('longitude')
        # quantity = request.POST.get('quantity')
        table = Table.objects.get(id=table_id)
        menu_item = MenuItem.objects.get(id=menu_id)
        receiver_id = request.user.id
        receiver = CustomUser.objects.get(id=receiver_id)
        order = Order.objects.create(table=table, ordered_time=datetime.datetime.now(), menu_items=menu_item,
                                     order_receiver=receiver, longitude=longitude, latitude=latitude)
        order.save()
        user_type = User_type.objects.get(id=1)
        message = f"There is a {menu_item.name} request at table number {table.table_number}"
        Messages.objects.create(sender=receiver, order=order, message=message, receiver_category=user_type)
    return redirect('manage_menu_item')


def my_order(request):
    user = request.user
    orders = Order.objects.filter(order_receiver=user)
    myorders = []
    for order in orders:
        primary_image = MenuImage.objects.filter(menu_item=order.menu_items).first()
        myorders.append({
            'orders': order,
            'menuimage': primary_image
        })
    return render(request, f"{user_validator(request)}/myorder.html", {'myorders': myorders})


def order_details(request, order_id):
    order = Order.objects.get(id=order_id)
    return render(request, "order_details.html", {"order": order})


def process_order(request, id):
    order = Order.objects.get(id=id)
    order.order_processor = request.user
    order.start_processing_time = datetime.datetime.now()
    order.save()
    return redirect('home')


def send_order(request, id):
    order = Order.objects.get(id=id)
    order.send = True
    order.received_time = datetime.datetime.now()  
    try:
        cupon_exist = Cupon.objects.get(customer = order.order_receiver, menu_item = order.menu_items)
    
        cupon_exist.ammount += order.menu_items.price/11
        cupon_exist.save()
    except:        
        Cupon.objects.create(customer = order.order_receiver, ammount = order.menu_items.price/11, menu_item = order.menu_items)
    order.save()
    return redirect('home')


def waiter_activity_check(request):
    orders = Order.objects.all()
    return render(request, f"{user_validator(request)}/waiter_activity_check.html", {'orders': orders})


def manage_sale(request):
    orders = Order.objects.all()
    return render(request, f"{user_validator(request)}/manage_sales.html", {'orders': orders})


def add_ingredient(request):
    if request.method == "POST":
        ingredient_name = request.POST['ingredient_name']
        quantity = float(request.POST['quantity'])
        measure = request.POST['measure']
        menu_id = request.POST['menu_id']
        price_one = float(request.POST['price'])

        menu_item = MenuItem.objects.get(id=menu_id)
        Ingredient.objects.create(ingredient_name=ingredient_name, quantity=quantity, measured_in=measure,
                                  price=price_one * quantity, menu_item=menu_item)
    return redirect('manage_ingredient')


def manage_ingredient(request):
    menu_items = MenuItem.objects.all().order_by('-name')
    ingredients = Ingredient.objects.all().order_by('-menu_item')
    return render(request, f"{user_validator(request)}/manage_ingredients.html",
                  {'ingredients': ingredients, 'menu_items': menu_items})


def delete_ingredient(request, id):
    ingredient = Ingredient.objects.get(id=id)
    ingredient.delete()
    return redirect("manage_ingredient")


def edit_ingredient(request, id):
    if request.method == "POST":
        ingredient_name = request.POST['ingredient_name']
        quantity = float(request.POST['quantity'])
        measure = request.POST['measure']
        menu_id = request.POST['menu_id']
        price_one = float(request.POST['price'])

        menu_item = MenuItem.objects.get(id=menu_id)
        ingredient = Ingredient.objects.get(id=id)
        ingredient.ingredient_name = ingredient_name
        ingredient.quantity = quantity
        ingredient.measured_in = measure
        ingredient.price = price_one * quantity
        ingredient.menu_item = menu_item
        ingredient.save()
    return redirect("manage_ingredient")


def cart(request, menu_id):
    menu_item = MenuItem.objects.get(id=menu_id)
    menu_image = MenuImage.objects.filter(menu_item = menu_item).first()
    tables = Table.objects.all()
    return render(request, "cart.html", {"menu_item":menu_item, "tables":tables, "menu_image":menu_image})

def my_cupon(request):
    my_cupons = Cupon.objects.filter(customer = request.user)
    cupons = []
    for cupon in my_cupons:
        cupon.image = MenuImage.objects.filter(menu_item = cupon.menu_item).first()
        cupons.append(cupon)
    return render(request, f"{user_validator(request)}/cupon.html", {'cupons':cupons})


# from django.shortcuts import render
# from django.http import HttpResponse
# from django_daraja.mpesa.core import MpesaClient

# def pay(request):
#     cl = MpesaClient()
#     # Use a Safaricom phone number that you have access to, for you to be able to view the prompt.
#     phone_number = '0765106833'
#     amount = 1
#     account_reference = 'reference'
#     transaction_desc = 'Description'
#     callback_url = 'https://api.darajambili.com/express-payment'
#     response = cl.stk_push(phone_number, amount, account_reference, transaction_desc, callback_url)
#     return HttpResponse(response)

import json
from django.shortcuts import redirect, render
from django.http import HttpResponse
from azampay import Azampay

def initiate_payment(request):
    # ... your order/payment logic ...
        object = Azampay(
            app_name = "Akacha",
            client_id= "ce8ece8a-da0c-4738-b9a4-f5c4b287b58a",
            client_secret='NX7Tw83XBifEVMA8ci3QQc6w/3Jsx/n0qsVwhz3kAaST6a950VQ6r/UTrFGQyY7UYlHhKCedFWv9E5mZ1DWz09Bj7tDEWWs/HMQQZRGLBg+bF0tFpfRIFYvE+XuH34bKbGZ8GinBi4NApiiHzgo5fTqjdVjhTeOKvoYgkdpHMqai31o+xvP5xjlxhWTDQDqwpRGDhwdQVYwZFDMglA3OGOtgYNO72OvO4Nx5mcGG4hoVBvkI6jj4DqyW/1uBpdP2xxpu0/Ycc3jHRAjVsYW5hI67XMYIcxcizoqnMERYYTYdjOc1f3UGb//U1H+URTCp/zoqlw6c0Rdhr1+u8vukKDQVt19JoV3XjAzNoQGasnckzYJkpVTu2D3Jdu7nz3jI5KMK5QpFakjZasN1xbVgm/FDpA3leAURo9DvvMqSRFlhoyBnDHhEp/N+Q1jgqQctU4hI41OWkLJlnOGwZVvfFU15wdbKRoKA7rHHHoH6YHwtRhxYP5ooAP23xKxWdGWy5HLZlKH7EcdwokIbOdb6d2tr8sXkr5iC65XFu6JykkQHuWCyi7QPfJRXrufVs1DmlXUbvucG5O4VZHTgja7T0paXe3M+WA90OQSyjbFUlAKtu+h95S1jRXOJttcjsrGd/9p8xmjchPIkHtFL9X0OZIIM37oRuYaX9aKmRdssrnQ=',
        )
        payment = object.mobile_checkout(
            amount="1000",
            # currency='12',
            # description='Order #123',
            external_id="https://akacha-restaurant.onrender.com",
            provider="Airtel",
            # additional_properties = 'Pay now',
            # customer_email=user.email,  # If available
            mobile='+255695570470',  # Replace with the actual phone number
            # ... other optional parameters (refer to AzamPay documentation) ...
        )
        return HttpResponse(payment)

        # return render(request, 'error.html', {'error_message': str(e)})

def payment_callback(request):
    order = 1
    Azampay = Azampay(order)
    transaction_id = request.GET.get('transaction_id')
    payment_status = request.GET.get('payment_status')

    try:
        # Verify payment status with AzamPay API (refer to documentation)
        verification_response = Azampay.verify_payment(transaction_id)

        if verification_response['status'] == 'success':
            # Update order status or perform other actions
            # order.status = 'paid'
            # order.save()

            return render(request, 'payment_success.html')
        else:
            # Handle payment failure
            return render(request, 'payment_failure.html')

    except Exception as e:
        return HttpResponse(json.dumps({'error': str(e)}), status=500)
