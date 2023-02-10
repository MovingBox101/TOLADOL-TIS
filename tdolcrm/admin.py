from django.contrib import admin

#from django.contrib import admin

from .models import Contact
from .models import Prospect 
from .models import Customer
from .models import Shipment_order
from .models import Shipment
from .models import Assortment
from .models import Case 
from .models import Employee_Records, Branch , Campaign , Activities , Invoice , User, Lead


# Register your models here.
admin.site.register(Contact)
admin.site.register(Prospect)
admin.site.register(Customer)
admin.site.register(Shipment_order)
admin.site.register(Shipment)
admin.site.register(Assortment)
admin.site.register(Case)
admin.site.register(Employee_Records)
admin.site.register(Branch)
admin.site.register(Campaign)
admin.site.register(Activities)
admin.site.register(Invoice)
admin.site.register(Lead)
admin.site.register(User)

