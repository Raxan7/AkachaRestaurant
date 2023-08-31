from django.shortcuts import render, redirect
from django.contrib import messages
from .models import CustomUser
from .EmailBackEnd import EmailBackEnd

# Create your views here.
def login(request):
    if request.method=="POST":
        username=request.POST.get('email')
        password=request.POST.get('password')
        user = EmailBackEnd.authenticate(request, username, password)
        if user != None:
            login(request, user)
            return redirect("home")
    return render(request, 'login.html')

def register(request):
    if request.method == "POST":
        first_name = request.POST.get("firstname")
        last_name = request.POST.get("lastname")
        email = request.POST.get("email")
        password = request.POST.get("password")
        password2 = request.POST.get("password1")
        if password != password2:
            messages.error(request, 'Password do not match')
            return render(request, 'register.html')
        if CustomUser.objects.filter(email=email).exists():
            messages.error(request, 'Email Alredy Exists')
            return render(request, 'register.html')
        try:
            user = CustomUser.objects.create_user(
                username=email, 
                email=email, 
                password=password,
                first_name=first_name,
                last_name=last_name,
            )
            user.save()
        except:
            messages.error(request, 'Something Went Wrong ')
            return render(request, 'register.html')
        return redirect("login")
    else:
        return render(request, 'register.html')
    
def home(request):
    return render(request, "home.html")