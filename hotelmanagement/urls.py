
from django.urls import path, include
from . import views

# https://docs.djangoproject.com/en/4.0/ref/templates/language/#id1


urlpatterns = [
    path("", views.logins, name="login"),
    path("register", views.register, name="register"),
    path("home", views.home, name="home"),
    path("logout", views.logout_user, name="logout"),
    path("add_user", views.add_user, name="add_user"),
    path("manage_user/<int:user>", views.manage_user, name="manage_user"),
    path("userprofile/<int:id>", views.userprofile, name="userprofile"),
    path("edit_user", views.edit_user, name="edit_user"),
    path("delete_user/<int:id>", views.delete_user, name="delete_user"),
    path("deactivate_user/<int:id>", views.deactivate_user, name="deactivate_user"),
    path("activate_user/<int:id>", views.activate_user, name="activate_user"),
]
