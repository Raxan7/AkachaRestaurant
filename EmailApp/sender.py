from django.core.mail import send_mail
from django.urls import reverse


def send_confirmation_email(user):
    confirmation_token = user.confirmation_token
    confirmation_url = reverse("confirm_email", args=[confirmation_token])

    message = f"Click the following link to confirm your email: {confirmation_url}"

    send_mail(
        "Confirm your email",
        message,
        "akacha@gmail.com",
        [user.email],
        fail_silently=False,
    )