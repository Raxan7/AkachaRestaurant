from django.contrib import messages
from django.contrib.auth import get_user_model
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.utils.http import urlsafe_base64_decode

from .token import account_activation_token
from hotelmanagement.models import CustomUser

from django.utils.encoding import force_str


# def confirm_email(request, confirmation_token):
#     try:
#         user = CustomUser.objects.get(confirmation_token=confirmation_token)
#         user.is_active = True
#         user.save()
#         return redirect("login")
#     except Exception as e:
#         print(e)
#         return HttpResponse("Invalid Confirmation Token")


def activate(request, uidb64, token):
    User = get_user_model()
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        messages.success(request, 'Thank you for your email confirmation. Now you can login your account.')
        return redirect("login")
    else:
        return HttpResponse('Activation link is invalid!')
