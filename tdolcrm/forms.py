from django import forms 
from .models import Contact
from django.urls import reverse_lazy
from crispy_forms.helper import FormHelper

class ContactForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        

    class Meta:
        model = Contact
        fields = ('Contact_ID', 'Last_Name', 'First_Name', 'Email_Address', 'Company_Name', 'Address_1', 'Birthdate')
