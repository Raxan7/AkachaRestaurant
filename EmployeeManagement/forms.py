from django import forms
from .models import *

## all models form fields goes here
class DepartmentsForm(forms.ModelForm):
    class Meta:
        model =Departments
        fields='__all__'
        


class employeesDetailsForm(forms.ModelForm):
    class Meta:
        model = EmployeeDetails
        fields ='__all__'
        
class EmploymentDetailForm(forms.ModelForm):
    class Meta:
        model = EmploymentDetail
        fields = '__all__'
        
class employee_addressForm(forms.ModelForm):
    class Meta:
        model = employee_address
        fields = '__all__'

class MainStoreForm(forms.ModelForm):
    class Meta:
        model = MainStore
        fields = '__all__'

class AllocateForm(forms.ModelForm):
    class Meta:
        model = OrderAlocation
        fields = fields = ['QuantityAllocated', 'Received_By', 'Issued_by', 'Receiver_department', 'Received_Condition']
