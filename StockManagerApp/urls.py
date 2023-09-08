from django.urls import path
from . import views

urlpatterns = [
    path('food_items/', views.food_item_list, name='food_item_list'),
    path('food_items/add/', views.add_food_item, name='add_food_item'),
    path('food_items/<int:pk>/', views.view_food_item, name='view_food_item'),
    path('food_items/<int:pk>/edit/', views.edit_food_item, name='edit_food_item'),
]
