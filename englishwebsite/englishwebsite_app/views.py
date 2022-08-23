from multiprocessing import context
from django.shortcuts import render
from englishwebsite_app.models import User
from django.shortcuts import  render, redirect
from .forms import UserRegisterForm
from django.contrib.auth import login
from django.contrib import messages

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
	if request.method == 'POST':
		form = UserRegisterForm(request.POST)
		if form.is_valid():
			login(request, user= form.save())
			username = form.cleaned_data['username']
			messages.success(request, f'Usuario {username} creado')
			return redirect('/homelogin')
	else:
		form = UserRegisterForm()
        

	context = { 'form' : form }
	return render(request, 'register.html', context)



def ejemplo_form_pelado(request):
    print("los datos son:", request.POST)
    return render(
        request, "ejemplo_form_pelado.html", {}
    )