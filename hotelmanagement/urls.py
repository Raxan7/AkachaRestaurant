
from django.urls import path, include
from . import views

# https://docs.djangoproject.com/en/4.0/ref/templates/language/#id1


urlpatterns = [
    path("", views.login, name="login"),
    path("register", views.register, name="register"),
    path("home", views.home, name="home")
]