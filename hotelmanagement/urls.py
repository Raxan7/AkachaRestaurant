
from django.urls import path, include
from . import views

# https://docs.djangoproject.com/en/4.0/ref/templates/language/#id1


urlpatterns = [
    path("", views.logins, name="login"),
    # path("login", views.logins, name="login"),

    # path('accounts/profile/', views.profile, name='profile'),
    # path("register", views.CustomRegistrationView.as_view(), name="register"),
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
    path("deactivate_all_user", views.deactivate_all_user, name="deactivate_all_user"),
    path("activate_all_user", views.activate_all_user, name="activate_all_user"),
    
    path("add_menu_category", views.add_menu_category, name="add_menu_category"),
    path("edit_menu_category/<int:id>", views.edit_menu_category, name = "edit_menu_category"),
    path("manage_menu_category", views.manage_menu_category, name="manage_menu_category"),
    
    path("add_menu_item", views.add_menu_item, name="add_menu_item"),
    path("edit_menu_item/<int:id>", views.edit_menu_item, name = "edit_menu_item"),
    path("manage_menu_item", views.manage_menu_item, name="manage_menu_item"),
     path("menu_item_description/<int:item_id>", views.menu_item_description, name="menu_item_description"),
    
    path("add_menu_image", views.add_menu_image, name="add_menu_image"),
    path("edit_menu_image/<int:id>", views.edit_menu_image, name = "edit_menu_image"),
    path("manage_menu_image", views.manage_menu_image, name="manage_menu_image"),
    path("get_items", views.get_items, name="get_items"),
    
    path("add_table", views.add_table, name="add_table"),
    path("manage_table", views.manage_table, name="manage_table"),
    
    path("add_order", views.add_order, name = "add_order"),
    path("my_order", views.my_order, name = "my_order"),
    path("process_order/<int:id>", views.process_order, name="process_order"),
    path("send_order/<int:id>", views.send_order, name="send_order"),
    
    path("waiter_activity_check", views.waiter_activity_check, name="waiter_activity_check"),
    
    path("manage_sale", views.manage_sale, name = "manage_sale"),
]
