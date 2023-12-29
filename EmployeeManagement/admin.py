# admin.py
from django.contrib import admin
from .models import *

def get_model_fields(self, model):
    return [field.name for field in model._meta.fields]    

class EmployeeDetailsAdmin(admin.ModelAdmin):
    list_display = get_model_fields(EmployeeDetails)
    search_fields = get_model_fields(EmployeeDetails)
    # list_filter = ('')
    ordering = get_model_fields(EmployeeDetails)
    # readonly_fields = ('')
admin.site.register(EmployeeDetails, EmployeeDetailsAdmin)

