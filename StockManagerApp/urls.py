from django.urls import path
from . import views

appname = "StockManagerApp"
urlpatterns = [
    path('food_items/', views.food_item_list, name='food_item_list'),
    path('food_items/add/', views.add_food_item, name='add_food_item'),
    path('food_items/<int:pk>/', views.view_food_item, name='view_food_item'),
    path('food_items/<int:pk>/edit/', views.edit_food_item, name='edit_food_item'),
    path('manage_sales/', views.manage_sales, name='manage_sales'),
    path('register_purchases/', views.purchase_registration, name='purchases_register'),
    path('purchases_list/', views.purchases_list_view, name='purchases_list'),
    path('purchases_detail/<int:pk>', views.purchases_detail, name='view_purchase_item'),
    path('request_foods/', views.request_food_items_view, name='request_food_items'),
    path('use_food_item/', views.use_food_item, name='use_food_item'),
]
