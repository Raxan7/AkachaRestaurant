from django.shortcuts import render

# Create your views here.
from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *
from django.template import loader
from .forms import *
from django.core.files.storage import FileSystemStorage
from hotelmanagement.models import CustomUser

# Create your views here.
def index(request):
   return render(request, 'index.html')

def inerpage(request):
       return render(request, 'inner-page.html')
    
#Akacha views displays here.

#This views calculate all total expenses from the main store.
def TotalExpenses():
       total_expenses = MainStore.objects.aggregate(models.Sum('BuyPrice'))['BuyPrice__sum'] or 0
       return total_expenses

#This views calculates the total income for all departments
def TotalIncome():
       total_income = Income.objects.aggregate(models.Sum('IncomeAmount'))['IncomeAmount__sum'] or 0
       return total_income

#This views calculates the total profit for all departments
def TotalProfitForDepartments():
       total_income = Income.objects.aggregate(models.Sum('IncomeAmount'))['IncomeAmount__sum'] or 0
       total_expenses = MainStore.objects.aggregate(models.Sum('BuyPrice'))['BuyPrice__sum'] or 0
       total_profit = total_income - total_expenses
       return total_profit
    
def allCalculatedExpenses(request):
       expenses = TotalExpenses()
       income = TotalIncome()
       profit = TotalProfitForDepartments()
       expensesDetails = MainStore.objects.all()
       incomeDetails = Income.objects.all()
       context={
          'expenses':expenses,
          'income':income,
          'profit':profit,
          'incomeDetails':incomeDetails,
          'expensesDetails':expensesDetails
       }
       return render(request,'AllExpenses.html',context)
    
# def department_register(request):
#        if request.method =='POST':
#               form =  DepartmentsForm(request.POST)
#               if form.is_valid():
#                      form.save()
#                      return redirect('registered_dept')
#        else:
#             form = DepartmentsForm()
#        return render(request,'employee/department_register.html',{'department':form})


def department_register(request):
       if request.method == 'POST':
              departmentID=request.POST.get('departmentID')
              departmentName=request.POST.get('departmentName')
              new_department=Departments(departmentID=departmentID, departmentName=departmentName)
              new_department.save()
              return redirect('registered_dept')
       return render(request, 'employee/department_register.html')
              
    
def registered_dept(request):
       registered_dept = Departments.objects.all()
       context={
          'registered':registered_dept
       }
       return render(request, 'employee/registered_dept.html', context)

# def EmployeesRegister(request):
#        if request.method == 'POST':
#               form = employeesDetailsForm(request.POST)
#               if form.is_valid():
#                      form.save()
#                      return redirect('EmployeeDetails')
#        else:
#             form = employeesDetailsForm()
#        return render(request,'employee/EmployeeRegister.html',{'employees':form})

def EmployeesRegister(request):
       departments = Departments.objects.all()
       if request.method=='POST':
              employeeId=request.POST.get('employeeId')
              firstname=request.POST.get('firstname')
              middlename = request.POST.get('middlename')
              lastname = request.POST.get('lastname')
              gender = request.POST.get('gender')
              dob = request.POST.get('dob')
              nssf=request.POST.get('nssf')
              nida = request.POST.get('nida')
              department = request.POST.get('department')
              employeesDetails = EmployeeDetails(employeeID=employeeId,firstName=firstname,middleName=middlename,
                                                 lastName=lastname,gender=gender,date_of_birth=dob,social_security_number=nssf,
                                                 National_id_number=nida)
              employeesDetails.save()
              return redirect('EmployeesRegister/')
       return render(request, 'employee/EmployeeRegister.html',{'departments':departments})
              
              

def employeesDetails(request):
       employee = EmployeeDetails.objects.all()
       context={
              'employ': employee
       }
       return render(request,'employee/EmployeesDetails.html', context)


def EmploymentRegister(request):
       if request.method == 'POST':
              form = EmploymentDetailForm(request.POST)
              if form.is_valid():
                     form.save()
                     return redirect('EmploymentDetail')
       else:
            form = EmploymentDetailForm()
       return render(request,'EmploymentRegisterl.html',{'employment':form})

def EmployeeDelete(request, pk):
       employee = EmployeeDetails.objects.get(employeeID=pk)
       if request.method == 'POST':
              employee.delete()
              return redirect('employeesDetails')
       return render(request, 'employeesDetails.html', {'employee': employee})


def EmploymentDetails(request):
       employments = EmploymentDetail.objects.all()
       context={
              'employments':employments
       }
       return render(request,'EmploymentDetail.html',context)

def employeeAddressesRegister(request):
       if request.method == 'POST':
              form = employee_addressForm(request.POST)
              if form.is_valid():
                     form.save()
                     return redirect('employeeAddress')
       else:
              form = employee_addressForm()
       return render(request, 'employeeAddressRegister.html', {'Address': form})

def employeeAddress(request):
       Address = employee_address.objects.all()
       context = {
              'Address': Address
              }
       return render(request, 'employeeAddress.html',context)

def MainStoteDetail(request):
       store = MainStore.objects.all()
       context={
              'store':store
       }
       return render(request, 'MainStoreDetail.html',context)

def MainStoreRegister(request):
       if request.method == 'POST':
              form = MainStoreForm(request.POST)
              if form.is_valid():
                     form.save
                     return redirect('MainStoreDetails')
       else: 
             form = MainStoreForm()
       return render(request, 'MainStore.html', {'MainStore': form})


def OrderProcessed(request):
       order =OrderAlocation.objects.all()
       context={
              'order': order
       }
       return render(request, 'OrderProcessed.html', context)

def AllocateItem(request,pk):
       items = MainStore.objects.get(ItemId=pk)
       context={
              'items': items
       }
       return render(request, 'AllocateItem.html', context)

def Allocate(request, pk):
       allocateItem = MainStore.objects.get(ItemId=pk)
       
       if request.method == 'POST':
              form = AllocateForm(request.POST)
              if form.is_valid():
                     allocation = form.save(commit=False)
                     allocation.ItemCategory=allocateItem.ItemCategory
                     allocation.ItemId = allocateItem
                     allocation.Item_name = allocateItem.Item_name
                     allocation.Unit_Measure = allocateItem.Unit_Measure      
                     Quantity_allocated = allocation.QuantityAllocated
                     Quantity_remained = allocateItem.RemainedQuantityInStock
                     if Quantity_allocated <= Quantity_remained:
                            allocation.save()
                            allocateItem.RemainedQuantityInStock -= allocation.QuantityAllocated
                            allocateItem.save()
                            return redirect('OrderProcessed')
                     else:
                            error_message = "Allocation failed.Please check the quantity in stock and try again..."
              else:
                     error_message = "Allocation failed. Please check the quantity and try again."
       else:
            form = AllocateForm(initial={'ItemId': allocateItem})
            error_message = None
       return render(request, 'order_allocate.html',{'allocate':form,'allocateItem': allocateItem,'error_message': error_message})


# def LegalDocumentsUpload(request):
#     if request.method == 'POST':
#         form = LegalDocumentUpload(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return redirect('success')
#     else:
#         form = LegalDocumentUpload()
#     return render(request, 'employee/UploadLegalDocuments.html', {'form': form})

# def success(request):
#     return render(request, 'success.html')

# views.py

def LegalDocumentsUpload(request):
    employees=EmployeeDetails.objects.all()
    if request.method == 'POST':
        job_application_letter = request.FILES.get('job_application_letter')
        sponsor_letter = request.FILES.get('sponsor_letter')
        local_approval_letter = request.FILES.get('local_government_approval_letter')
        curriculum_vitae = request.FILES.get('cv')

        # Process the form data as needed
        # For example, save the files to the media directory
        fs = FileSystemStorage()
        fs.save(f'LegalDocuments/{job_application_letter.name}', job_application_letter)
        fs.save(f'LegalDocuments/{sponsor_letter.name}', sponsor_letter)
        fs.save(f'LegalDocuments/{local_approval_letter.name}', local_approval_letter)
        fs.save(f'LegalDocuments/{curriculum_vitae.name}', curriculum_vitae)

        success_message="uploadess successfully"

    return render(request, 'employee/UploadLegalDocuments.html',{'employees':employees})

              
              
              
# import secrets
# import string
# import random

# def generate_random_string(length=5):
#     alphabet = string.ascii_letters + string.digits
#     random_string = ''.join(secrets.choice(alphabet) for _ in range(length))
#     return random_string

# # Example usage
# random_string = generate_random_string()
# print(random_string)

# def copy(request):
#        users = CustomUser.objects.all()
#        gender = ["Male", "Female", "Other"]
#        for user in users:
#               EmployeeDetails.objects.create(
#                      user = user,
#                      employeeID = generate_random_string(5),
#                      gender = random.choice(gender),
#                      department = Departments.objects.get(departmentID = "12"),
#                      social_security_number=generate_random_string(10),
#                      National_id_number=generate_random_string(8),
#               )
#        return HttpResponse("Ready")
       