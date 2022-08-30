from django.shortcuts import  render, redirect
from .forms import UserRegisterForm
from django.contrib.auth import login
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.

def base(request):
    return render(request,'base.html',)

@login_required
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

@login_required
def writing(request):
	return render(request,'writing.html')

@login_required
def reading(request):
	return render(request,'reading.html')

@login_required
def listening(request):
	return render(request,'listening.html')

@login_required
def grammarExercices(request):
	return render(request,'grammar-exercises.html')

@login_required
def alphabetExercises(request):
	return render(request,'alphabet-exercises.html')

@login_required
def articlesExercises(request):
	return render(request,'articles.html')

@login_required
def vocabularyExercises(request):
	return render(request,'vocabulary-exercises.html')

@login_required
def nacionalitiesExercisesAtoC(request):
	return render(request,'countries-nationalitiesAtoC.html')

@login_required
def nacionalitiesExercisesCtoH(request):
	return render(request,'countries-nationalitiesC-H.html')