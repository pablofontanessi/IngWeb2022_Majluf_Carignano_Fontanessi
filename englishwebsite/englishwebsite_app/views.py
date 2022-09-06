from unicodedata import category
from django.shortcuts import  render, redirect
from .models import Post, Exercise_Category
from .forms import UserRegisterForm, CreateNewExercise
from django.contrib.auth import login
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, DetailView

# Create your views here.W

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
	WrittingExercises = Post.objects.filter(category =1)
	return render(request,'writing.html',{'exercise_list': WrittingExercises})


@login_required
def reading(request):
	ReadingExercises = Post.objects.filter(category = 3)
	return render(request,'reading.html',{'exercise_list': ReadingExercises})

@login_required
def listening(request):
	ListeningExercises = Post.objects.filter(category = 2)
	return render(request,'listening.html',{'exercise_list': ListeningExercises})
@login_required
def speaking(request):
	SpeakingExercises = Post.objects.filter(category = 4)
	return render(request,'speaking.html',{'exercise_list': SpeakingExercises})

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


@login_required
def create_exercise(request):
	if request.method == 'POST':
		form = CreateNewExercise(request.POST,request.FILES)
		
		if form.is_valid():
			
			form.save()
			return redirect('/homelogin')
	else:
		form = CreateNewExercise()
		 
	
	
	return render(request,'createExercises.html', {'form':form})