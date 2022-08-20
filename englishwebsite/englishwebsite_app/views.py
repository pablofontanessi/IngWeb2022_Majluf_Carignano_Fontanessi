from django.shortcuts import render, HttpResponseRedirect
from englishwebsite_app.models import User
from datetime import datetime

#from englishwebsite_app.forms import FormularioNoticia, FormularioModeloNoticia

# Create your views here.

def inicio(request):
    nueva = User()
    nueva.first_name = 'Hola'
    nueva.last_name = 'Usuario'
    nueva.birthdate = datetime.now()
    


    return render(
        request,
        'home.html',
    )

def ejemplo_form_pelado(request):
    print("los datos son:", request.POST)
    return render(
        request, "ejemplo_form_pelado.html", {}
    )