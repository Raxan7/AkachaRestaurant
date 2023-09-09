from django.contrib import admin
from .models import Stock


@admin.register(Stock)
class StockAdmin(admin.ModelAdmin):
    list_display = ('name', 'quantity', 'expiration_date',)
    # list_filter = ('is_low_inventory',)
    search_fields = ('name',)
