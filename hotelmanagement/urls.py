
from django.urls import path, include
from . import views

# https://docs.djangoproject.com/en/4.0/ref/templates/language/#id1


urlpatterns = [
    path("", views.logins, name="login"),
    path("register", views.register, name="register"),
    path("home", views.home, name="home"),
    path("logout", views.logout_user, name="logout"),
    path("add_user", views.add_user, name="add_user"),
    path("add_user_type", views.add_user_type, name="add_user_type"),
    path("manage_user/<int:id>", views.manage_user, name="manage_user"),
    path("userprofile/<int:id>", views.userprofile, name="userprofile"),
    path("edit_user", views.edit_user, name="edit_user"),
    path("delete_user/<int:id>", views.delete_user, name="delete_user"),
    path("deactivate_user/<int:id>", views.deactivate_user, name="deactivate_user"),
    path("activate_user/<int:id>", views.activate_user, name="activate_user"),
    
    path("add_menu_category", views.add_menu_category, name="add_menu_category"),
    path("edit_menu_category/<int:id>", views.edit_menu_category, name = "edit_menu_category"),
    path("manage_menu_category", views.manage_menu_category, name="manage_menu_category"),
    
    path("add_menu_item", views.add_menu_item, name="add_menu_item"),
    path("edit_menu_item/<int:id>", views.edit_menu_item, name = "edit_menu_item"),
    path("manage_menu_item", views.manage_menu_item, name="manage_menu_item"),
    
    path("add_menu_image", views.add_menu_image, name="add_menu_image"),
    path("edit_menu_image/<int:id>", views.edit_menu_image, name = "edit_menu_image"),
    path("manage_menu_image", views.manage_menu_image, name="manage_menu_image"),
]
