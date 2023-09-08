from django.contrib import admin
from .models import Reservation, Restaurant, Review, MenuCategory, MenuItem, Order, OrderItem, Employee, Payment
# Register your models here.


admin.site.register(Reservation)
admin.site.register(Restaurant)
admin.site.register(Review)
admin.site.register(MenuCategory)
admin.site.register(MenuItem)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(Employee)
admin.site.register(Payment)