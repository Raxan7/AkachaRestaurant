from django.shortcuts import render, redirect
from django.contrib import messages
from .models import CustomUser
from .EmailBackEnd import EmailBackEnd
from django.contrib.auth import login, logout
from .models import *
from .user_validator import user_validator
from django.http import JsonResponse
from django.core.files.storage import FileSystemStorage
from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Avg
import datetime
from django.http import JsonResponse
from django.contrib.auth import update_session_auth_hash

# Create your views here.
def logins(request):
    if request.method=="POST":
        username=request.POST.get('email')
        password=request.POST.get('password')
        user = EmailBackEnd.authenticate(request, username, password)
        if user != None:
            login(request, user)
            return redirect('home')
    return render(request, "login.html")


def home(request):
    return render(request, f"{user_validator(request)}/home.html")

def userprofile(request, id):
    user = CustomUser.objects.get(id=id)
    return render(request, f"{user_validator(request)}/user_details.html", {'userr':user})

def logout_user(request):
    logout(request)
    return redirect("login")

def add_user_type(request):
    if request.method=="POST":
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
        fullname = first_name+last_name
        if CustomUser.objects.filter(username=fullname).exists():
            fullname = email
        if password != password1:
            messages.error(request, 'Password do not match')
            return render(request, "register.html")
        if CustomUser.objects.filter(email=email).exists():
            messages.error(request, 'Email Alredy Exists')
            return render(request, "register.html")
        user = CustomUser.objects.create_user(user_type=user_type, username=fullname, email=email, password=password,first_name=first_name,last_name=last_name,)
        user.save()
        return redirect("login")
    else:
        return render(request, "register.html")

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

    return render(request, 'password_change.html', {'base_template':base_template})


def delete_user(request, id):
    user = CustomUser.objects.get(id=id)
    user.delete()
    if user.user_type == "Super":
        return redirect("manage_user", 2)
    else:
        return redirect("manage_user", 1)

#0 means all user types present
def activate_all_user(request):
    users = CustomUser.objects.exclude(user_type=1)
    for user in users:
        user.is_active = True
        user.save()
    return redirect("manage_user", 0)  
 
 #0 means all user types present
def deactivate_all_user(request):
    users = CustomUser.objects.exclude(user_type=1)
    for user in users:
        user.is_active = False
        user.save()
    return redirect("manage_user", 0)       

def deactivate_user(request, id):
    user = CustomUser.objects.get(id=id)
    if user.user_type != "CEO":
            user.is_active=False
            user.save()
    user.save()
    user_type = user.user_type
    user_types=User_type.objects.get(user_type = user_type)
    type_id = user_types.id
    return redirect("manage_user", type_id)
    

def activate_user(request, id):
    user = CustomUser.objects.get(id=id)
    user.is_active=True
    user.save()
    user_type = user.user_type
    user_types=User_type.objects.get(user_type = user_type)
    type_id = user_types.id
    return redirect("manage_user", type_id)

def add_user(request):
    if request.method == "POST":
        first_name = request.POST.get("firstname")
        last_name = request.POST.get("lastname")
        email = request.POST.get("email")
        user_types = request.POST.get("user_type")
        user_type = User_type.objects.get(id = user_types)
        password = "12345678"
        fullname = first_name+last_name
        if CustomUser.objects.filter(username=fullname).exists():
            fullname = email
        if CustomUser.objects.filter(email=email).exists():
            messages.error(request, 'Email Alredy Exists')
            return render(request, f"{user_validator(request)}/add_user.html")
        user = CustomUser.objects.create_user(user_type=user_type, username=fullname, email=email, password=password,first_name=first_name,last_name=last_name,)
        user.save()
    return render(request, f"{user_validator(request)}/add_user.html")

def  manage_user(request, id):
    if id==0:
        users=CustomUser.objects.all()
    else:
        users=CustomUser.objects.filter(user_type=id)
    return render(request, f"{user_validator(request)}/manage_user.html", {'users':users})

def edit_user(request):
    if request.method == "POST":
        first_name = request.POST.get("firstname")
        last_name = request.POST.get("lastname")
        email = request.POST.get("email")
        username = request.POST.get("username")
        user_types = request.POST.get("user_type")
        profile = request.FILES.get("image")
        id = request.POST.get("id")
        user_type = User_type.objects.get(id = user_types)
        user = CustomUser.objects.get(id=id)
        user.first_name=first_name
        user.last_name = last_name
        user.email = email
        user.username = username
        user.user_type = user_type
        if profile:
            user.profile = profile
        user.save()
        return redirect('userprofile', id=id)

def add_menu_category(request):
    if request.method == "POST":
        name = request.POST['menu_name']
        MenuCategory.objects.create(name = name)
        return redirect("manage_menu_category")

def manage_menu_category(request):
    menus = MenuCategory.objects.all()
    return render(request, f"{user_validator(request)}/manage_menu.html", {"menus":menus})

def edit_menu_category(request, id):
    if request.method == "POST":
        name = request.POST['name']
        menu = MenuCategory.objects.get(id=id)
        menu.name=name
        name.save()
        return redirect("/")
    menu = MenuCategory.objects.get(id=id)
    return render(request, f"{user_validator(request)}/edit_menu_category.html", {"menu":menu})
    
def add_menu_item(request):
    if request.method == "POST":
        category_id = request.POST["category_id"]
        name = request.POST['item_name']
        description = request.POST['description']
        price = float(request.POST['price'])
        category = MenuCategory.objects.get(id=category_id)
        MenuItem.objects.create(name=name, description=description, price=price,category=category)
    categories = MenuCategory.objects.all()
    return render(request, f"{user_validator(request)}/add_menu_item.html", {'menucategories':categories})

def manage_menu_item(request):
    menuItems = MenuItem.objects.all().order_by('-name')
    menu_items = []
    for menuitem in menuItems:
        menuitem.profit = menuitem.price - menuitem.cost
        primary_image = MenuImage.objects.filter(menu_item=menuitem).first()
        menu_items.append({
            'menuitems':menuitem,
            'menuimage':primary_image
        })
    tables = Table.objects.all()
    return render(request, f"{user_validator(request)}/manage_menu_item.html", {'menu_items':menu_items, 'tables':tables})

def menu_item_description(request, item_id):
    menuitem = MenuItem.objects.get(id = item_id)
    images = MenuImage.objects.filter(menu_item = menuitem)
    return render(request, f"{user_validator(request)}/menu_description.html", {'images':images, 'menuitem':menuitem})


# views.py
from django.http import JsonResponse
from django.shortcuts import get_object_or_404

def rate_menu_item_ajax(request, menu_item_id):
    if request.method == 'POST':
        menu_item = get_object_or_404(MenuItem, pk=menu_item_id)
        has_rated = MenuItemRating.objects.filter(user=request.user, menu_item=menu_item).exists()

        if not has_rated:
            rating = int(request.POST.get('rating'))
            menu_item_rating = MenuItemRating(user=request.user, menu_item=menu_item, rating=rating)
            menu_item_rating.save()

            # Calculate and update the average rating for the menu item
            menu_item.average_rating = MenuItemRating.objects.filter(menu_item=menu_item).aggregate(Avg('rating'))['rating__avg']
            menu_item.save()

            return JsonResponse({'message': 'Rating submitted successfully'})
        else:
            return JsonResponse({'message': 'You have already rated this item'})
    else:
        return JsonResponse({'message': 'Invalid request'})



def edit_menu_item(request, id):
    if request.method == "POST":
        menuItem = MenuItem.objects.get(id=id)
        category_id = request.POST["category_id"]
        name = request.POST['name']
        description = request.POST['description']
        price = request.POST['price']
        category = MenuCategory.objects.get(id=category_id)
        menuItem.name = name
        menuItem.description=description
        menuItem.price=price
        menuItem.category=category
        menuItem.save()
        return redirect("/")
    menu_item = MenuItem.objects.get(id=id)
    return render(request, f"{user_validator(request)}/edit_menu_item.html", {"menu_item":menu_item})

def add_menu_image(request):
    if request.method == "POST":
        menu_id = request.POST['menu_id']
        image = request.FILES['image']
        menu = MenuItem.objects.get(id = menu_id)
        MenuImage.objects.create(menu_item = menu, image=image)
        return redirect("add_menu_image")
    menuitems = MenuItem.objects.all()
    return render(request, f"{user_validator(request)}/add_menu_image.html", {'menuitems':menuitems})

#ajax to get menu items when adding imge
def get_items(request):
    category_id = request.GET.get('category_id')
    items = MenuItem.objects.filter(menucategory__id = category_id).values('id', 'name')
    return JsonResponse({'items': list(items)})

def manage_menu_image(request):
    menu_images = MenuImage.objects.all()
    return render(request, f"{user_validator(request)}/manage_menu_image.html", {'images': menu_images})

def edit_menu_image(request, id):
    if request.method == "POST":
        menu_id = request.POST['menu_id']
        category_id = request.POST["category_id"]
        image = request.FILES['image']
        category = MenuCategory.objects.get(id=category_id)
        menu = MenuItem.objects.get(id = menu_id)
        menu_image = MenuImage.objects.get(id=id)
        if image:
            menu_image.image=image
        menu_image.menu_item=menu
        menu_image.menu_category = category
        menu_image.save()
        return redirect("edit_menu_image", id)
    menu_image = MenuImage.objects.get(id=id)
    return render(request, f"{user_validator(request)}/edit_menu_image.html", {'menu_image':menu_image})

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
    return render(request, f"{user_validator(request)}/manage_restaurant.html", {"restaurants":restaurants})

def edit_restaurant(request, id):
    if request.method == "POST":
        restaurant = Restaurant.objects.get(id=id)
        name = request.POST['name']
        location = request.POST['location']
        description = request.POST['description']
        contact = request.POST['contact']
        restaurant.name=name
        restaurant.location = location
        restaurant.description=description
        restaurant.contact=contact
        restaurant.save()
        return redirect("/")
    restaurant = Restaurant.objects.get(id=id)
    return render(request, f"{user_validator(request)}/edit_restaurant.html", {"restaurant":restaurant})

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
    return render(request, f"{user_validator(request)}/manage_table.html", {'tables':tables})

def add_order(request):
    if request.method == "POST":
        table_id = request.POST.get('table_id')
        menu_id = request.POST.get('menu_id')
        # quantity = request.POST.get('quantity')
        table = Table.objects.get(id = table_id)
        menu_item = MenuItem.objects.get(id = menu_id)
        receiver_id = request.user.id
        receiver = CustomUser.objects.get(id = receiver_id)
        order = Order.objects.create(table = table, ordered_time = datetime.datetime.now() , menu_items=menu_item, order_receiver = receiver)
        order.save()
        user_type = User_type.objects.get(id = 1)
        message = f"There is a {menu_item.name} request at table number {table.table_number}"
        Messages.objects.create(sender = receiver, order= order, message=message, receiver_category=user_type )
    return redirect('manage_menu_item')
        
def my_order(request):
    user = request.user
    orders = Order.objects.filter(order_receiver = user)
    myorders=[]
    for order in orders:
        primary_image = MenuImage.objects.filter(menu_item=order.menu_items).first()
        myorders.append({
            'orders':order,
            'menuimage':primary_image
        })
    return render(request, f"{user_validator(request)}/myorder.html", {'myorders':myorders})

def process_order(request, id):
    order = Order.objects.get(id = id)
    order.order_processor = request.user
    order.start_processing_time = datetime.datetime.now()
    order.save()
    return redirect('home')

def send_order(request, id):
    order = Order.objects.get(id = id)
    order.send = True
    order.received_time = datetime.datetime.now()
    order.save()
    return redirect('home')

def waiter_activity_check(request):
    orders = Order.objects.all()
    return render(request, f"{user_validator(request)}/waiter_activity_check.html", {'orders':orders})

def manage_sale(request):
    orders = Order.objects.all()
    return render(request, f"{user_validator(request)}/manage_sales.html", {'orders':orders})

def add_ingredient(request):
    if request.method == "POST":
        ingredient_name = request.POST['ingredient_name']
        quantity = float(request.POST['quantity'])
        measure = request.POST['measure']
        menu_id = request.POST['menu_id']
        price_one= float(request.POST['price'])
        
        menu_item  = MenuItem.objects.get(id = menu_id)
        Ingredient.objects.create(ingredient_name=ingredient_name, quantity=quantity, measured_in = measure, price = price_one * quantity, menu_item = menu_item )
    return redirect('manage_ingredient')

def manage_ingredient(request):
    menu_items = MenuItem.objects.all().order_by('-name')
    ingredients = Ingredient.objects.all().order_by('-menu_item')
    return render(request, f"{user_validator(request)}/manage_ingredient.html", {'ingredients':ingredients, 'menu_items': menu_items})
