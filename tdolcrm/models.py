from django.db import models

# Create your models here.
from django.utils.text import gettext_lazy as _
from django.contrib.auth.models import AbstractUser
from django.urls import reverse

class User(AbstractUser):
    pass

class Contact (models.Model): 
    Contact_ID = models.BigAutoField(primary_key=True)
    Last_Name = models.CharField(max_length=50)
    First_Name = models.CharField(max_length=50)
    Email_Address = models.EmailField(max_length=50)
    Company_Name = models.CharField(max_length=50)
    Address_1=models.CharField(max_length=250)
    Birthdate=models.DateField()

    
    def __str__(self):
        self.full_name = self.First_Name + " " + self.Last_Name
        return  self.full_name


class Prospect (Contact):
    Nature_of_Business = models.CharField(max_length=50)
    Nature_of_Shipment = models.CharField(max_length=50)
    Pickup_location = models.CharField(max_length=17)
    NoOfPackages_Monthly = models.IntegerField()
    Monthly_revenue = models.IntegerField()

    def __str__(self):
        self.full_name = self.First_Name + " " + self.Last_Name
        return self.full_name
 


class Lead (Contact):
    Lead_Source = (
        ('Coldcall', 'Coldcall'),
        ('Campaign', 'Campaign'),
        ('Email', 'Email'),
        ('Word of Mouth', 'Word of Mouth'),
        ('Website', 'Website'),
        ('Tradeshow', 'Tradeshow'),
        ('Direct mail', 'Direct mail'),
        ('Employee referral', 'Employee referral'),
        ('Self generated', 'Self generated'),
        ('Existing customer', 'Existing customer'),
        ('Other', 'Other',)
    )

    Leads = models.CharField(max_length=25, choices=Lead_Source)
    # associate a Lead to a Sales Resource
    # associate a Lead to a Customer Service Executive

class Customer (Prospect):
    Customer_ID = models.BigAutoField (primary_key=True)
    Consignee_Name = models.CharField(max_length=50)
    Consignee_Company = models.CharField(max_length=50)
    Address = models.CharField(max_length=50)
    No_of_packages_monthly = models.IntegerField()


class Shipment_order(Customer):
    Consignee_telephone = models.IntegerField()
    No_of_packages = models.IntegerField()
    Dimensional_weight = models.IntegerField()
    Dimensional_height = models.IntegerField()
    Item_description = models.TextField(max_length=250)
    Customer_signature = models.CharField(max_length=250)
    customers = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='topic_content_type') #this generated an error without the @related_name

class Shipment(models.Model):
    Tracking_id = models.IntegerField(primary_key=True)
    Shipmentorder1 = models.OneToOneField(Shipment_order, on_delete=models.CASCADE, related_name='ships')

    EscalationReasons = (
        ('MISDECLARATION' ,'Misdeclaration'),
        ('THEFT', 'Theft'),
        ('Delays', 'Delays'),
        ('Specify Others', 'Specify Others'),
    )
    Escalation = models.CharField(max_length=20, choices=EscalationReasons)

class Assortment (models.Model):
    Item_label = models.CharField(max_length=30)
    pictures = models.FileField()
    uploaded_at = models.DateTimeField(auto_now_add=True)
    shipmentorder = models.OneToOneField(Shipment_order, on_delete=models.CASCADE)

    class Item_qty(models.IntegerChoices):
        ONE = 1
        TWO = 2
        THREE = 3
        FOUR = 4
        FIVE = 5
        SIX = 6
        SEVEN = 7
        EIGHT = 8
        NINE = 9
        TEN = 10

    AMOUNT_OF_QTY_SHIPPED= models.IntegerField(choices=Item_qty.choices)

#class Shipment (models.Model):
 #   Tracking_No = models.IntegerField()

 #this assigns a shipment to many Cases. 

class Case(models.Model):
    Date_processed = models.DateTimeField()
    Case_description = models.CharField(max_length=500)
    Shipments = models.ForeignKey(Shipment, on_delete=models.CASCADE)
    Case_Categories = models.OneToOneField(Shipment, on_delete=models.PROTECT, related_name='categories')

# This is a record of all employees. It will be expounded upon after further meeting with the HR Officers
class Employee_Records (models.Model):
    Employee_ID = models.IntegerField(primary_key=True)
    Employee_Name = models.CharField(max_length=100)
    Employment_date = models.DateField()
    Resumption_date = models.DateField()
    # create a relationship between the employee_records and the branch (one to one rel)

class Designations (models.Model):
    Designation = (
        
        ('Customer Service Executive', 'Customer Service Executive'),
        ('Human Resources', 'Human Resources'),
        ('Sales Resource', 'Sales Resource'),
        ('Operations Officer', 'Operations Officer'),
        ('Marketing Officer', 'Marketing Officer'),
        ('Management', 'Management'),
    )

    Designations = models.CharField(max_length=30, choices=Designation)


class Sales_Resource(models.Model):
    user=models.OneToOneField(User, on_delete=models.PROTECT)

class Customer_Service_Executive(models.Model):
    user = models.OneToOneField(User, on_delete=models.PROTECT)

    def __str__(self):
        return self.user.email

class Human_Resource(models.Model):
    user = models.OneToOneField(User, on_delete=models.PROTECT)
   
class Branch (models.Model):
    Branches = (
        ('Ikeja' , 'Ikeja' ),
        ('Gbagada', 'Gbagada'),
        ('Surulere', 'Surulere'),
    )
    ##################################################################################################
    employee_info = models.OneToOneField(User, on_delete = models.CASCADE)
    customer_info = models.OneToOneField(Customer, on_delete = models.CASCADE)
    branches_loc = models.CharField(max_length=8, choices=Branches)
    branch_employees = models.ForeignKey(Employee_Records, on_delete = models.CASCADE, related_name="content_type")
    #include branch as a choice

class Campaign(models.Model):
    Date_created = models.DateTimeField()
    Start_date = models.DateField()
    End_date = models.DateField()
    Budget = models.IntegerField()
    Actual_cost = models.IntegerField()
    Expected_revenue = models.IntegerField()
    Campaign_objective = models.IntegerField()
    Campaign_description = models.TextField(max_length=300)
   

class Activities (models.Model):
    Activity_name = models.CharField(max_length=100)
    Date_created1=models.DateField()
    Start_date1=models.DateField()
    End_date1=models.DateField()
    Employee_assigned = models.ForeignKey(User, on_delete=models.CASCADE)
    Activity_description = models.TextField(max_length=300)
    Campaign_Activities = models.ForeignKey(Campaign, on_delete=models.PROTECT)
    
class Invoice (models.Model):
    Invoice_ID = models.IntegerField(primary_key=True)
    Consignee_Name_inv = models.OneToOneField(Customer, on_delete = models.PROTECT)
    Invoice_date = models.DateTimeField(auto_now_add=True)
    Shipment_origin = models.CharField(max_length=40)
    No_of_packages1 = models.IntegerField()
    Total_Billable_weight = models.IntegerField()
    Tracking_numbers = models.OneToOneField(Shipment, on_delete = models.PROTECT)
    Insurance_choice = (
        ('Yes', 'Yes'),
        ('No' , 'No'),
    )
    Insurances = models.CharField(max_length=3 ,choices=Insurance_choice)
    Packaging_fee = models.IntegerField()
    Freight_cost = models.IntegerField()
    Total_shipment_cost = models.IntegerField()



