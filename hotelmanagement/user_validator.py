from django.shortcuts import render, redirect


def user_validator(request):
    if request.user.is_authenticated:
        user_type = request.user.user_type
        return user_type
    else:
        return redirect('login')
