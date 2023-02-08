from django.shortcuts import render, redirect
from .models import Lead
from django.http import HttpResponse
from django.contrib.auth.models import User, auth

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
