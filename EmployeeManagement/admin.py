# admin.py
from django.contrib import admin
from .models import EmployeeDetails

class EmployeeDetailsAdmin(admin.ModelAdmin):
    list_display = ('employeeID', 'social_security_number', 'gender', 'date_of_birth','National_id_number')
    search_fields = ('employeeID', 'social_security_number','National_id_number')
    list_filter = ('employeeID','National_id_number')
    ordering = ('employeeID','social_security_number')
    readonly_fields = ('gender')
admin.site.register(EmployeeDetails, EmployeeDetailsAdmin)
