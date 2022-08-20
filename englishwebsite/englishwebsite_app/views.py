from django.shortcuts import render
from englishwebsite_app.models import User

# Create your views here.

def base(request):
    return render(
        request,
        'base.html',
    )

def homelogin(request):
    return render(
        request,
        'homelogin.html',
    )

def register(request):
    return render(
        request,
        'register.html',
    )

def ejemplo_form_pelado(request):
    print("los datos son:", request.POST)
    return render(
        request, "ejemplo_form_pelado.html", {}
    )