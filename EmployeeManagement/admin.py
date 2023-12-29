# admin.py
from django.contrib import admin
from .models import Departments

class DepartmentsAdmin(admin.ModelAdmin):
    list_display = ('field1', 'field2')  # Fields to be displayed in the list view
    search_fields = ('field1', 'field2')  # Enable searching by these fields
    list_filter = ('field2',)  # Add filters for these fields
    ordering = ('field1',)  # Set the default sorting order

    fieldsets = (
        ('Main Information', {
            'fields': ('field1', 'field2'),
        }),
        # Add more fieldsets as needed
    )

    # Customize how fields are displayed in the detail view
    readonly_fields = ('field1',)  # Fields that are read-only in the detail view

admin.site.register(Departments, DepartmentsAdmin)
