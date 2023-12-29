from django.urls import path
from .import views

appname = 'EmployeeManagement'
urlpatterns = [
    path('', views.index, name='index'),
    path('innerpage/',views.inerpage,name='iner-page'),
    path('AllExpenses/',views.allCalculatedExpenses, name ='allCalculatedExpenses'),
    path('department_register/',views.department_register, name ='department_register'),
    path('registered_dept/',views.registered_dept, name ='registered_dept'),
    path('EmployeesRegister/',views.EmployeesRegister, name='EmployeesRegister'),
    path('EmployeeDetails/',views.employeesDetails, name='EmployeeDetails'),
    path('EmploymentRegister/',views.EmploymentRegister, name='EmploymentRegister'),
    path('EmploymentDetail/',views.EmploymentDetails, name='EmploymentDetail'),
    path('employeeAddressesRegister/',views.employeeAddressesRegister, name='employeeAddressesRegister'),
    path('employeeAddress/',views.employeeAddress, name='employeeAddress'),
    path('EmploymentDetail/<str:pk>/',views.EmployeeDelete, name='EmployeeDelete'),
    path('MainStoreDetails/',views.MainStoteDetail,name='MainStoreDetails'),
    path('OrderProcessed/',views.OrderProcessed,name='OrderProcessed'),
    path('MainStore/',views.MainStoreRegister,name='MainStore'),
    path('allocateItem/<int:pk>/',views.AllocateItem,name='AllocateItem'),
    path('allocate/<int:pk>/',views.Allocate,name='allocate'),
    path('LegalDocumentsUpload/',views.LegalDocumentsUpload,name='LegalDocumentsUpload'),
    
    # path('copy', views.copy, name="copy"),
]
