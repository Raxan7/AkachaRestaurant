from django.utils.crypto import get_random_string


confirmation_token = get_random_string(length=32)