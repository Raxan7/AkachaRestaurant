from typing import Any
from django.db import models
from django.core.validators import MinValueValidator
from cloudinary.models import CloudinaryField
from hotelmanagement.models import CustomUser
from datetime import date
  
class Departments(models.Model):
    departmentID=models.CharField(max_length=20,primary_key=True)
    departmentName=models.CharField(max_length=100,unique=True)
    def __str__(self):
        return self.departmentName
  
#model for register employee parsonal details
GENDER_CHOICE = (
      ('male','male'),
      ('female','female'),
      ('other','other')
  )
class EmployeeDetails(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    employeeID = models.CharField(max_length=100,primary_key=True)
    # firstName = models.CharField(max_length=100,blank=False)
    # middleName = models.CharField(max_length=100,blank=False)
    # lastName = models.CharField(max_length=100,blank=False)
    gender = models.CharField(max_length=10,choices=GENDER_CHOICE)
    date_of_birth = models.DateField(default= date.today)
    social_security_number = models.CharField(max_length=20)
    National_id_number = models.CharField(max_length=15)
    department = models.ForeignKey(Departments,on_delete=models.CASCADE)
    # def __str__(self):
    #     return self.firstName
    
class EmploymentDetail(models.Model):
    employee = models.OneToOneField(EmployeeDetails, on_delete=models.CASCADE)
    job_title = models.CharField(max_length=50)
    date_of_hire = models.DateField()
    employment_status = models.CharField(max_length=20)
    def __str__(self):
        return self.job_title

    
class employee_address(models.Model):
    employee = models.OneToOneField(EmployeeDetails,on_delete=models.CASCADE)
    RegionOfBirth = models.CharField(max_length=100)
    DistrictOfBirth = models.CharField(max_length=100)
    wardOfBirth = models.CharField(max_length=100)
    CurrentRegion = models.CharField(max_length=100)
    CurrentDistrict = models.CharField(max_length=100)
    CurrentWard = models.CharField(max_length=100)
    def __str__(self):
        return self.CurrentRegion
        
class EmployeeContact(models.Model):
    employee = models.ForeignKey(EmployeeDetails,on_delete=models.CASCADE)
    phoneNumber = models.CharField(max_length=13,unique=True)
    Email_Address = models.EmailField(max_length=100,unique=True)
    def __str__(self):
        return self.phoneNumber

    
class EmergencyContact(models.Model):
    employee = models.ForeignKey(EmployeeDetails, on_delete=models.CASCADE)
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    relationship = models.CharField(max_length=50)
    Valid_phoneNumber = models.CharField(max_length=13,unique=True)
    Valid_Email_Address = models.EmailField(max_length=100,unique=True)
    def __str__(self):
        return self.relationship

    
    
class EquipmentIssuance(models.Model):
    employee = models.ForeignKey(EmployeeDetails, on_delete=models.CASCADE)
    uniform_details = models.TextField()
    equipment_issuance_date = models.DateField()
    equipment_return_date = models.DateField(auto_now=True)
    def __str__(self):
        return self.uniform_details

class LegalDocuments(models.Model):
    employee = models.OneToOneField(EmployeeDetails, on_delete=models.CASCADE)
    Job_Application_Letter = CloudinaryField("image")
    SponsorLetter = CloudinaryField("image")
    Local_government_Approval_Letter = CloudinaryField("image")
    Curriculam_vitae = CloudinaryField("image")
    def __str__(self):
        return self.employee
    
DAYS_OF_WEEK = (
    ('Monday', 'Monday'),
    ('Tuesday', 'Tuesday'),
    ('Wednesday', 'Wednesday'),
    ('Thursday', 'Thursday'),
    ('Friday', 'Friday'),
    ('Saturday', 'Saturday'),
    ('Sunday', 'Sunday'),
)
    
class WorkSchedule(models.Model):
    employee = models.ForeignKey(EmployeeDetails, on_delete=models.CASCADE)
    work_hours = models.DecimalField(max_digits=5,decimal_places=2,validators=[MinValueValidator(0)],default=0)
    days_off =models.CharField(max_length=10, choices=DAYS_OF_WEEK)
    overtime_hours = models.DecimalField(max_digits=5, decimal_places=2,blank=True,validators=[MinValueValidator(0)],default=0)
    Month = models.DateField(auto_now=True)
    def __str__(self):
        return str(self.work_hours)

class ExitRecords(models.Model):
    employee = models.OneToOneField(EmployeeDetails, on_delete=models.CASCADE)
    exit_date = models.DateField()
    exit_reason = models.TextField()
    def __str__(self):
        return self.exit_date  

class UnitOfMeasure(models.Model):
    UnitName = models.CharField(max_length=20, primary_key=True)
    def __str__(self):
        return self.UnitName

CONDITION_CHOICES = (
    ('good', 'Good'),
    ('damaged', 'Damaged'),
    ('faulty', 'Faulty'),
)

class ItemCategory(models.Model):
    CategoryName = models.CharField(max_length=100, primary_key=True)
    def __str__(self):
        return self.CategoryName
    
class MainStore(models.Model):
     ItemCategory = models.ForeignKey(ItemCategory, on_delete=models.CASCADE)
     ItemId = models.AutoField(primary_key=True)
     Item_name = models.CharField(max_length=100,blank=False)
     Unit_Measure = models.ForeignKey(UnitOfMeasure, on_delete=models.CASCADE)
     BuyPrice = models.DecimalField(max_digits=20, decimal_places=2,validators=[MinValueValidator(0)])
     ReceivedQuantityInStock =models.DecimalField(max_digits=20, decimal_places=2,validators=[MinValueValidator(0)],default=0)
     RemainedQuantityInStock =models.DecimalField(max_digits=20,decimal_places=2,validators=[MinValueValidator(0)],default=0)
     Received_By = models.ForeignKey(EmployeeDetails,on_delete=models.CASCADE)
     Received_date = models.DateField(auto_now_add=True)
     Received_Condition=models.CharField(max_length=10,choices=CONDITION_CHOICES)
         
     
class OrderAlocation(models.Model):
    ItemCategory = models.ForeignKey(ItemCategory, on_delete=models.CASCADE)
    ItemId = models.ForeignKey(MainStore, on_delete=models.CASCADE,default=0)
    Item_name = models.CharField(max_length=100,blank=False)
    Unit_Measure = models.ForeignKey(UnitOfMeasure, on_delete=models.CASCADE)
    QuantityAllocated = models.DecimalField(max_digits=20, decimal_places=2,validators=[MinValueValidator(0)])
    Received_By = models.ForeignKey(EmployeeDetails,on_delete=models.CASCADE)
    Issued_by = models.CharField(max_length=100,blank=False)
    Received_date = models.DateField(auto_now=True)
    Receiver_department = models.ForeignKey(Departments,on_delete=models.CASCADE)
    Received_Condition=models.CharField(max_length=10,choices=CONDITION_CHOICES)
        
    
class Income(models.Model):
       IncomeCategoryName = models.ForeignKey(ItemCategory,on_delete=models.CASCADE)
       date = models.DateField(auto_now = True)
       IncomeAmount = models.DecimalField(max_digits=10, decimal_places=2)   

    
class EquipmentCategory(models.Model):
    CategoryName = models.CharField(max_length=100, primary_key=True) 
    
class EquipmentDetails(models.Model):
    CategoryName=models.ForeignKey(EquipmentCategory,on_delete=models.CASCADE)
    EquipmentID = models.CharField(max_length=100,primary_key=True)
    EquipmentName = models.CharField(max_length=20)
    EquipmentCondition = models.CharField(max_length=15,choices=CONDITION_CHOICES)
    Location = models.CharField(max_length=100,blank=True)
    