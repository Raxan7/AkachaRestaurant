# admin.py
from django.contrib import admin
from .models import EmployeeDetails

class EmployeeDetailsAdmin(admin.ModelAdmin):
    list_display = ('employeeID', 'social_security_number', 'gender', 'date_of_birth','National_id_number')  # Fields to be displayed in the list view
    search_fields = ('employeeID', 'social_security_number','National_id_number')  # Enable searching by these fields
    list_filter = ('employeeID','National_id_number')  # Add filters for these fields
    ordering = ('employeeID','social_security_number')  # Set the default sorting order

    fieldsets = (
        ('Main Information', {
            'fields': ('employeeID', 'National_id_number'),
        }),
        # Add more fieldsets as needed
    )

    # Customize how fields are displayed in the detail view
    readonly_fields = ('gender')  # Fields that are read-only in the detail view

admin.site.register(EmployeeDetails, EmployeeDetailsAdmin)
