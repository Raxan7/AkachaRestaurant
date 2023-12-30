from django.shortcuts import render, redirect
from django.http import HttpResponseForbidden, HttpResponse
import uuid
from django.utils import timezone
from django.core.mail import EmailMessage

from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.conf import settings
from django.contrib import messages
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode

def send_reset_email(request, user, to_email, token):
    subject = 'Password Reset'
    message = render_to_string('password_reset_email.html', {'token': token})
    plain_message = strip_tags(message)  # Remove HTML tags for plain text email
    # from_email = "no-reply-akacha@raxan7.com"
    # recipient_list = [to_email]
    current_site = get_current_site(request)
    message = render_to_string('password_reset_email.html', {
            'user': user,
            'domain': current_site.domain,
            'uid': urlsafe_base64_encode(force_bytes(user.pk)),
            'token': user.reset_password_token,
        })
    email = EmailMessage(
        subject=subject,
        body=message,
        from_email="no-reply-akacha@raxan7.com",
        to=[to_email]
    )
    email.send()

def generate_reset_token():
    return str(uuid.uuid4())


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
