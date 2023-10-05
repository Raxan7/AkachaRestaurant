from django.contrib.auth.decorators import login_required
from django.contrib.sites.shortcuts import get_current_site
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib import messages
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode

from EmailApp.token import account_activation_token
from .models import CustomUser
from .EmailBackEnd import EmailBackEnd
from django.contrib.auth import login, logout

from django.utils.encoding import force_bytes
from django.core.mail import EmailMessage


from .models import User_type, Reservation, MenuImage, Restaurant, Review, MenuCategory, MenuItem, Order, OrderItem, \
    Employee, Payment, Table
from .user_validator import user_validator


# Create your views here.
def logins(request):
    if request.method == "POST":
        username = request.POST.get('email')
        password = request.POST.get('password')
        user = EmailBackEnd.authenticate(request, username, password)
        if user != None:
            login(request, user, backend='django.contrib.auth.backends.ModelBackend')
            return redirect('home')
    return render(request, "login.html")


def home(request):
    return render(request, f"{user_validator(request)}/home.html")


def userprofile(request, id):
    user = CustomUser.objects.get(id=id)
    return render(request, f"{user_validator(request)}/user_details.html", {'userr': user})


def logout_user(request):
    logout(request)
    return redirect("login")


@login_required
def profile(request):
    user = request.user
    return render(request, 'profile.html', {'user': user})


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
        if CustomUser.objects.filter(username=fullname).exists():
            fullname = email
        if password != password1:
            messages.error(request, 'Password do not match')
            return render(request, "register.html")
        if CustomUser.objects.filter(email=email).exists():
            messages.error(request, 'Email Alredy Exists')
            return render(request, "register.html")
        user = CustomUser.objects.create_user(user_type=user_type, username=fullname, email=email, password=password,
                                              first_name=first_name, last_name=last_name, )
        user.is_active = False
        user.save()

        current_site = get_current_site(request)
        mail_subject = 'Activation link has been sent to your email account'
        message = render_to_string('acc_active_email.html', {
            'user': user,
            'domain': current_site.domain,
            'uid': urlsafe_base64_encode(force_bytes(user.pk)),
            'token': account_activation_token.make_token(user),
        })
        to_email = email
        email = EmailMessage(
            mail_subject, message, to=[to_email]
        )
        email.send()
        return HttpResponse('Please confirm your email address to complete the registration')
        # return redirect("login")
    else:
        return render(request, "register.html")


def delete_user(request, id):
    user = CustomUser.objects.get(id=id)
    user.delete()
    if user.user_type == "Super":
        return redirect("manage_user", 2)
    else:
        return redirect("manage_user", 1)


def activate_all_user(request):
    users = CustomUser.objects.exclude(user_type=4)
    for user in users:
        user.is_active = True
    return redirect("manage_user", 0)


def deactivate_all_user(request):
    users = CustomUser.objects.exclude(user_type=4)
    for user in users:
        user.is_active = False
    return redirect("manage_user", 0)


def deactivate_user(request, id):
    user = CustomUser.objects.get(id=id)
    if user.user_type != "CEO":
        user.is_active = False
        user.save()
    user.save()
    user_type = user.user_type
    user_types = User_type.objects.get(user_type=user_type)
    type_id = user_types.id
    return redirect("manage_user", type_id)


def activate_user(request, id):
    user = CustomUser.objects.get(id=id)
    user.is_active = True
    user.save()
    user_type = user.user_type
    user_types = User_type.objects.get(user_type=user_type)
    type_id = user_types.id
    return redirect("manage_user", type_id)


def add_user(request):
    if request.method == "POST":
        first_name = request.POST.get("firstname")
        last_name = request.POST.get("lastname")
        email = request.POST.get("email")
        user_type = request.POST.get("user_type")
        password = "12345678"
        fullname = first_name + last_name
        if CustomUser.objects.filter(username=fullname).exists():
            fullname = email
        if CustomUser.objects.filter(email=email).exists():
            messages.error(request, 'Email Alredy Exists')
            return render(request, f"{user_validator(request)}/add_user.html")
        user = CustomUser.objects.create_user(user_type=user_type, username=fullname, email=email, password=password,
                                              first_name=first_name, last_name=last_name, )
        user.save()
    return render(request, f"{user_validator(request)}/add_user.html")


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
        user_type = request.POST.get("user_type")
        profile = request.FILES.get("image")
        id = request.POST.get("id")
        user = CustomUser.objects.get(id=id)
        user.first_name = first_name
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
        MenuCategory.objects.create(name=name)
        return redirect("manage_menu_category")


def manage_menu_category(request):
    menus = MenuCategory.objects.all()
    return render(request, f"{user_validator(request)}/manage_menu.html", {"menus": menus})


def edit_menu_category(request, id):
    if request.method == "POST":
        name = request.POST['name']
        menu = MenuCategory.objects.get(id=id)
        menu.name = name
        name.save()
        return redirect("/")
    menu = MenuCategory.objects.get(id=id)
    return render(request, f"{user_validator(request)}/edit_menu_category.html", {"menu": menu})


def add_menu_item(request):
    if request.method == "POST":
        category_id = request.POST["category_id"]
        name = request.POST['name']
        description = request.POST['description']
        price = request.POST['price']
        category = MenuCategory.objects.get(id=category_id)
        MenuItem.objects.create(name=name, description=description, price=price, category=category)
    return render(request, f"{user_validator(request)}/add_menu_item.html")


def manage_menu_item(request):
    menuItems = MenuItem.objects.all()
    return render(request, f"{user_validator(request)}/manage_menu_item.html", {'menuItems': menuItems})


def edit_menu_item(request, id):
    if request.method == "POST":
        menuItem = MenuItem.objects.get(id=id)
        category_id = request.POST["category_id"]
        name = request.POST['name']
        description = request.POST['description']
        price = request.POST['price']
        category = MenuCategory.objects.get(id=category_id)
        menuItem.name = name
        menuItem.description = description
        menuItem.price = price
        menuItem.category = category
        menuItem.save()
        return redirect("/")
    menu_item = MenuItem.objects.get(id=id)
    return render(request, f"{user_validator(request)}/edit_menu_item.html", {"menu_item": menu_item})


def add_menu_image(request):
    if request.method == "POST":
        menu_id = request.POST['menu_id']
        category_id = request.POST["category_id"]
        image = request.FILES['image']
        category = MenuCategory.objects.get(id=category_id)
        menu = MenuItem.objects.get(id=menu_id)
        MenuImage.objects.create(menu_item=menu, menu_category=category, image=image)
        return redirect("add_menu_image")
    menu_categories = MenuCategory.objects.all()
    return render(request, f"{user_validator(request)}/add_menu_image.html", {'categories': menu_categories})


def manage_menu_image(request):
    menu_images = MenuImage.objects.all()
    return render(request, f"{user_validator(request)}/manage_menu_image.html", {'images': menu_images})


def edit_menu_image(request, id):
    if request.method == "POST":
        menu_id = request.POST['menu_id']
        category_id = request.POST["category_id"]
        image = request.FILES['image']
        category = MenuCategory.objects.get(id=category_id)
        menu = MenuItem.objects.get(id=menu_id)
        menu_image = MenuImage.objects.get(id=id)
        if image:
            menu_image.image = image
        menu_image.menu_item = menu
        menu_image.menu_category = category
        menu_image.save()
        return redirect("edit_menu_image", id)
    menu_image = MenuImage.objects.get(id=id)
    return render(request, f"{user_validator(request)}/edit_menu_image.html", {'menu_image': menu_image})


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
        restaurant_id = request.POST["restaurant_id"]
        capacity = request.POST["capacity"]
        restaurant = Restaurant.objects.get(id=restaurant_id)
        Table.objects.create(table_number=table_number, restaurant=restaurant, capacity=capacity)
    return render(request, f"{user_validator(request)}/add_table.html")
