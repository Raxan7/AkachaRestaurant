from .models import User_type, Messages
from django.shortcuts import render, redirect

def user_type_list(request):
    user_type = User_type.objects.all()
    return {'user_types': user_type}

def message_analyser(request):
    try:
        user = request.user
        messages = Messages.objects.filter(receiver_category=user.user_type, order__send=False)
        return {'messagess':messages}
    except:
        
       user_type = User_type.objects.all()
       return {'user_types': user_type}