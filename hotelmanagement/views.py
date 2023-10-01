from django.shortcuts import render, redirect
from django.contrib import messages
from .models import CustomUser
from .EmailBackEnd import EmailBackEnd
from django.contrib.auth import login, logout
from .models import User_type ,Reservation, MenuImage, Restaurant, Review, MenuCategory, MenuItem, Order, OrderItem, Employee, Payment, Table

# Create your views here.
def logins(request):
    if request.method=="POST":
        username=request.POST.get('email')
        password=request.POST.get('password')
        user = EmailBackEnd.authenticate(request, username, password)
        if user != None:
            login(request, user)
            return redirect('home')
    return render(request, 'login.html')


def home(request):
    if request.user.is_authenticated:
        user_type = request.user.user_type
        return render(request, f"{user_type}/home.html")
    else:
        return redirect('login')

def userprofile(request, id):
    user = CustomUser.objects.get(id=id)
    return render(request, "user_details.html", {'userr':user})

def logout_user(request):
    logout(request)
    return redirect("login")

def add_user_type(request):
    if request.method=="POST":
        user_type = request.POST.get('user_type')
        User_type.objects.create(user_type=user_type)
    return redirect('/')

def register(request):
    if request.method == "POST":
        first_name = request.POST.get("firstname")
        last_name = request.POST.get("lastname")
        email = request.POST.get("email")
        password = request.POST.get("password")
        user_types = request.POST.get("user_type")
        if user_types != None:
            user_type = User_type.objects.get(id=user_types)
        else:
            user_type = User_type.objects.get(id=5)
        if password:
            password2 = request.POST.get("password1")
            if password != password2:
                messages.error(request, 'Password do not match')
                return render(request, 'register.html')
        else:
            password="12345678"
        if CustomUser.objects.filter(email=email).exists():
            messages.error(request, 'Email Alredy Exists')
            return render(request, 'register.html')
        try:
            user = CustomUser.objects.create_user(user_type=user_type, username=first_name + last_name, email=email, password=password,first_name=first_name,last_name=last_name,)
            user.save()
        except:
            messages.error(request, 'Something Went Wrong ')
            return render(request, 'register.html')
        if password=="12345678":
            messages.success(request, 'One Employee added successfully!')
            return redirect("add_user")
        return redirect("login")
    else:
        return render(request, 'register.html')

def delete_user(request, id):
    user = CustomUser.objects.get(id=id)
    user.delete()
    if user.user_type == "Super":
        return redirect("manage_user", 2)
    else:
        return redirect("manage_user", 1)

def deactivate_all_user(request):
    users = CustomUser.objects.all()
    for user in users:
        user.is_active=False
        user.save()
        

def deactivate_user(request, id):
    user = CustomUser.objects.get(id=id)
    user.is_active=False
    user.save()
    if user.user_type == "Super":
        return redirect("manage_user", 2)
    else:
        return redirect("manage_user", 1)

def activate_user(request, id):
    user = CustomUser.objects.get(id=id)
    user.is_active=True
    user.save()
    if user.user_type == "Super":
        return redirect("manage_user", 2)
    else:
        return redirect("manage_user", 1)

def add_user(request):
    return render(request, "add_user.html")

def  manage_user(request, id):
    users=CustomUser.objects.filter(user_type=id)
    return render(request, "manage_user.html", {'users':users})

def edit_user(request):
    if request.method == "POST":
        first_name = request.POST.get("firstname")
        last_name = request.POST.get("lastname")
        email = request.POST.get("email")
        username = request.POST.get("username")
        user_type = request.POST.get("user_type")
        profile = request.FILES.get("image")
        id = request.POST.get("id")
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
    return render(request, "manage_menu.html", {"menus":menus})

def edit_menu_category(request, id):
    if request.method == "POST":
        name = request.POST['name']
        menu = MenuCategory.objects.get(id=id)
        menu.name=name
        name.save()
        return redirect("/")
    menu = MenuCategory.objects.get(id=id)
    return render(request, "edit_menu_category.html", {"menu":menu})
    
def add_menu_item(request):
    if request.method == "POST":
        category_id = request.POST["category_id"]
        name = request.POST['name']
        description = request.POST['description']
        price = request.POST['price']
        category = MenuCategory.objects.get(id=category_id)
        MenuItem.objects.create(name=name, description=description, price=price,category=category)
    return render(request, "add_menu_item.html")

def manage_menu_item(request):
    menuItems = MenuItem.objects.all()
    return render(request, "manage_menu_item.html", {'menuItems':menuItems})

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
    return render(request, "edit_menu_item.html", {"menu_item":menu_item})

def add_menu_image(request):
    if request.method == "POST":
        menu_id = request.POST['menu_id']
        category_id = request.POST["category_id"]
        image = request.FILES['image']
        category = MenuCategory.objects.get(id=category_id)
        menu = MenuItem.objects.get(id = menu_id)
        MenuImage.objects.create(menu_item = menu, menu_category = category, image = image)
        return redirect("add_menu_image")
    menu_categories = MenuCategory.objects.all()
    return render(request, "add_menu_image.html", {'categories': menu_categories})

def manage_menu_image(request):
    menu_images = MenuImage.objects.all()
    return render(request, "manage_menu_image.html", {'images': menu_images})

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
    return render(request, "edit_menu_image.html", {'menu_image':menu_image})

def add_restaurant(request):
    if request.method == "POST":
        name = request.POST['name']
        location = request.POST['location']
        description = request.POST['description']
        contact = request.POST['contact']
        Restaurant.objects.create(name=name, location=location, description=description, contact=contact)
    return render(request, "add_restaurant.html")

def manage_restaurant(request):
    restaurants = Restaurant.objects.all()
    return render(request, "manage_restaurant.html", {"restaurants":restaurants})

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
    return render(request, "edit_restaurant.html", {"restaurant":restaurant})

def add_table(request):
    if request.method == "POST":
        table_number = request.POST["table_number"]
        restaurant_id = request.POST["restaurant_id"]
        capacity = request.POST["capacity"]
        restaurant = Restaurant.objects.get(id = restaurant_id)
        Table.objects.create(table_number=table_number, restaurant=restaurant, capacity=capacity)
    return render(request, "add_table.html")