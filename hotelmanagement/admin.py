from django.contrib import admin
from .models import *

def get_model_fields(self, model):
        return [field.name for field in model._meta.fields]

admin.site.register(Messages)
admin.site.register(Ingredient)
admin.site.register(MenuItemRating)
admin.site.register(CustomUser)
admin.site.register(Restaurant)
admin.site.register(Review)
admin.site.register(MenuCategory)
admin.site.register(MenuItem)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(Employee)
admin.site.register(Payment)
admin.site.register(MenuImage)
admin.site.register(User_type)
admin.site.register(Table)
admin.site.register(Cupon)


class MessagesAdmin(admin.ModelAdmin):
    list_display = get_model_fields(Messages)
    search_fields = get_model_fields(Messages)
    list_filter = ('')
    ordering = get_model_fields(Messages)
    readonly_fields = ('')
admin.site.register(Messages, MessagesAdmin)


class CuponAdmin(admin.ModelAdmin):
    list_display = get_model_fields(Cupon)
    search_fields = get_model_fields(Cupon)
    list_filter = ('')
    ordering = get_model_fields(Cupon)
    readonly_fields = ('')
admin.site.register(Cupon, CuponAdmin)

class IngredientAdmin(admin.ModelAdmin):
    list_display = get_model_fields(Ingredient)
    search_fields = get_model_fields(Ingredient)
    list_filter = ('')
    ordering = get_model_fields(Ingredient)
    readonly_fields = ('')
admin.site.register(Ingredient, IngredientAdmin)

class MenuItemRatingAdmin(admin.ModelAdmin):
    list_display = get_model_fields(MenuItemRating)
    search_fields = get_model_fields(MenuItemRating)
    list_filter = ('')
    ordering = get_model_fields(MenuItemRating)
    readonly_fields = ('')
admin.site.register(MenuItemRating, MenuItemRatingAdmin)

class CustomUserAdmin(admin.ModelAdmin):
    list_display = get_model_fields(CustomUser)
    search_fields = get_model_fields(CustomUser)
    list_filter = ('')
    ordering = get_model_fields(CustomUser)
    readonly_fields = ('')
admin.site.register(CustomUser, CustomUserAdmin)

class RestaurantAdmin(admin.ModelAdmin):
    list_display = get_model_fields(Restaurant)
    search_fields = get_model_fields(Restaurant)
    list_filter = ('')
    ordering = get_model_fields(Restaurant)
    readonly_fields = ('')
admin.site.register(Restaurant, RestaurantAdmin)

class ReviewAdmin(admin.ModelAdmin):
    list_display = get_model_fields(Review)
    search_fields = get_model_fields(Review)
    list_filter = ('')
    ordering = get_model_fields(Review)
    readonly_fields = ('')
admin.site.register(Review, ReviewAdmin)

class MenuCategoryAdmin(admin.ModelAdmin):
    list_display = get_model_fields(MenuCategory)
    search_fields = get_model_fields(MenuCategory)
    list_filter = ('')
    ordering = get_model_fields(MenuCategory)
    readonly_fields = ('')
admin.site.register(MenuCategory, MenuCategoryAdmin)

class MenuItemAdmin(admin.ModelAdmin):
    list_display = get_model_fields(MenuItem)
    search_fields = get_model_fields(MenuItem)
    list_filter = ('')
    ordering = get_model_fields(MenuItem)
    readonly_fields = ('')
admin.site.register(MenuItem, MenuItemAdmin)

class EmployeeAdmin(admin.ModelAdmin):
    list_display = get_model_fields(Employee)
    search_fields = get_model_fields(Employee)
    list_filter = ('')
    ordering = get_model_fields(Employee)
    readonly_fields = ('')
admin.site.register(Employee, EmployeeAdmin)

class PaymentAdmin(admin.ModelAdmin):
    list_display = get_model_fields(Payment)
    search_fields = get_model_fields(Payment)
    list_filter = ('')
    ordering = get_model_fields(Payment)
    readonly_fields = ('')
admin.site.register(Payment, PaymentAdmin)

class MenuImageAdmin(admin.ModelAdmin):
    list_display = get_model_fields(MenuImage)
    search_fields = get_model_fields(MenuImage)
    list_filter = ('')
    ordering = get_model_fields(MenuImage)
    readonly_fields = ('')
admin.site.register(MenuImage, MenuImageAdmin)

class User_typeAdmin(admin.ModelAdmin):
    list_display = get_model_fields(User_type)
    search_fields = get_model_fields(User_type)
    list_filter = ('')
    ordering = get_model_fields(User_type)
    readonly_fields = ('')
admin.site.register(User_type, User_typeAdmin)

class TableAdmin(admin.ModelAdmin):
    list_display = get_model_fields(Table)
    search_fields = get_model_fields(Table)
    list_filter = ('')
    ordering = get_model_fields(Table)
    readonly_fields = ('')
admin.site.register(Table, TableAdmin)
