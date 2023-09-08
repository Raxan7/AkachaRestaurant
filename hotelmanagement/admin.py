from django.contrib import admin
from .models import Reservation, Restaurant, Review, MenuCategory, MenuItem, Order, OrderItem, Employee, Payment, Stock
# Register your models here.


@admin.register(Stock)
class StockAdmin(admin.ModelAdmin):
    list_display = ('name', 'quantity', 'expiration_date', 'is_low_inventory')
    list_filter = ('is_low_inventory',)
    search_fields = ('name',)


admin.site.register(Reservation)
admin.site.register(Restaurant)
admin.site.register(Review)
admin.site.register(MenuCategory)
admin.site.register(MenuItem)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(Employee)
admin.site.register(Payment)