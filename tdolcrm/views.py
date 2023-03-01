from django.shortcuts import render, redirect
from .models import Lead
from .models import Contact
from .forms import ContactForm
from django.forms import ModelForm
from django.http import HttpResponse
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.views import generic
from .import models
from django.shortcuts import render, HttpResponse
from django.contrib.messages.views import SuccessMessageMixin
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field, HTML, Submit
from django import forms

# Createdef login(request):
def login(request):
    if request.method== 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect("/")
        else:
            messages.info(request, 'invalid credentials')
            return redirect ('login')
    else:
        return render(request, 'login.html')


def ContactPage (request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('login')
    else:
        form = ContactForm()
    return render(request, 'Contacts.html', {'form':form})



class ContactForm(ModelForm):
    Address_1 = forms.CharField(
        label = 'Address'
    )
    class Meta:
        model = models.Contact
        fields = ['Contact_ID', 'Last_Name', 'First_Name', 'Email_Address', 'Company_Name', 'Address_1','Birthdate']

    @property
    def helper(self):
        helper = FormHelper()
        helper.layout = Layout(
           HTML('<h4> Enter your Contact</h4>'),
            )
        for field in self.Meta().fields:
            helper.layout.append(
                Field(field, wrapper_class='row')
            )
        helper.layout.append(Submit('submit', 'Submit your contact', css_class='btn-success'))
        helper.field_class = 'col-9'
        helper.label_class = 'col-3'
       
        return helper 

class ProspectForm(ModelForm):
    Nature_of_Business = forms.CharField
    Last_Name =forms.CharField (
       label = 'Business Category' 
    )
    Last_Name = forms.CharField(
        label ='Last Name'
    )
    First_Name = forms.CharField(
        label = 'First Name'
    )


class CreateView(SuccessMessageMixin, generic.CreateView):
    template_name = 'Contacts.html'
    success_message = 'Your entry has been succesfully saved!'
    form_class = ContactForm








