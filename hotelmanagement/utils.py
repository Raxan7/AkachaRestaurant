from django.shortcuts import render, redirect
from django.http import HttpResponseForbidden, HttpResponse

def user_validator(request):
    if request.user.is_authenticated:
        user_type = request.user.user_type
        return user_type
    else:
        return redirect('login')

def ajax_validation(request):
    if request.method == "POST":
        return False
    elif request.method == "GET":
        return False
    else:
        return True
