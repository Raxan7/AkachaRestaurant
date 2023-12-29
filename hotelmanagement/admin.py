from django.contrib import admin
from .models import *


# admin.site.register(Messages)
# admin.site.register(Ingredient)
admin.site.register(MenuItemRating)
# admin.site.register(CustomUser)
admin.site.register(Restaurant)
admin.site.register(Review)
admin.site.register(MenuCategory)
# admin.site.register(MenuItem)
# admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(Employee)
admin.site.register(Payment)
admin.site.register(MenuImage)
admin.site.register(User_type)
admin.site.register(Table)
# admin.site.register(Cupon)

class MessagesAdmin(admin.ModelAdmin):
    list_display = ('sender', 'receiver_category','time_sent','time_opened', 'opened', 'message', 'message_type', 'order')
    search_fields = ('sender', 'receiver_category','message_type', 'order')
    list_filter = ('sender', 'receiver_category','message_type', 'order')
    ordering = ('sender', 'receiver_category','message_type', 'order')
    # readonly_fields = ('used')
admin.site.register(Messages, MessagesAdmin)

class CuponAdmin(admin.ModelAdmin):
    list_display = ('ammount', 'used','customer','menu_item')
    search_fields = ('ammount', 'used','customer','menu_item')
    list_filter = ('ammount', 'used')
    ordering = ('ammount', 'used', 'customer','menu_item')
    # readonly_fields = ('used')
admin.site.register(Cupon, CuponAdmin)

class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name','username','email','is_active')
    search_fields = ('first_name', 'last_name','username','email')
    list_filter = ('first_name', 'last_name','username','email')
    ordering = ('first_name', 'last_name','username','email')
    # readonly_fields = ('used')
admin.site.register(CustomUser, CustomUserAdmin)

class MenuItemAdmin(admin.ModelAdmin):
    list_display = ('category', 'name','description','price','average_rating', 'ingredient_cost', 'orders_number', 'item_profit')
    list_filter = ('category', 'name')
    search_fields = ('category', 'name')
    ordering = ('category', 'name','price','average_rating', 'ingredient_cost', 'orders_number', 'item_profit')
    # readonly_fields = ('used')
admin.site.register(MenuItem, MenuItemAdmin)

class OrderAdmin(admin.ModelAdmin):
    list_display = ('table', 'menu_items','ordered_time','start_processing_time', 'received_time', 'order_processor', 'order_receiver', 'longitude', 'latitude')
    search_fields = ('table', 'menu_items','order_processor', 'order_receiver')
    list_filter = ('table', 'menu_items','order_processor', 'order_receiver')
    ordering = ('table', 'menu_items','order_processor', 'order_receiver')
    # readonly_fields = ('used')
admin.site.register(Order, OrderAdmin)

class IngredientAdmin(admin.ModelAdmin):
    list_display = ('menu_item', 'ingredient_name','measured_in','quantity','price')
    search_fields = ('menu_item', 'ingredient_name')
    list_filter = ('menu_item','ingredient_name')
    ordering = ('menu_item', 'ingredient_name')
    # readonly_fields = ('used')
admin.site.register(Ingredient, IngredientAdmin)