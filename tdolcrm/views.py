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
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field, HTML, Submit

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


class CreateView(generic.CreateView):
    model = models.Contact
    fields = ['Contact', 'Contact_ID', 'Last_Name', 'First_Name',
     'Email_Address', 'Company_Name', 'Address_1', 'Birthdate']
    template_name = 'Contacts.html'





