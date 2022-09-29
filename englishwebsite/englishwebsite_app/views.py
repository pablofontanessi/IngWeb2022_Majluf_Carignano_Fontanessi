from django.shortcuts import  get_object_or_404, render, redirect
from .models import *
from .forms import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from django.http import HttpResponse  
from django.shortcuts import render, redirect  
from django.contrib.sites.shortcuts import get_current_site  
from django.utils.encoding import force_str, force_bytes
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode  
from englishwebsite_app.tokens import account_activation_token  
from django.core.mail import send_mail
from django.template.loader import render_to_string  
from django.conf import settings

# Create your views here.

def base(request):
    return render(request,'base.html',)

@login_required
def homelogin(request):
    return render(request,'homelogin.html',)

def register(request):
	if request.method == 'POST':
		form = UserRegisterForm(request.POST)
		if form.is_valid():
			# save form in the memory not in database  
				user = form.save(commit = False)  
				user.is_active = False  
				user.save()  
            # to get the domain of the current site  
				current_site = get_current_site(request)  
				mail_subject = 'English website - Activation link'  
				message = render_to_string(
					'acc_active_email.html', 
						{  
						'user': user,  
						'domain': current_site.domain,  
						'uid': urlsafe_base64_encode(force_bytes(user.pk)),  
						'token': account_activation_token.make_token(user),  
						},
					)
			
				to_email = form.cleaned_data.get('email')  
				
				send_mail(
                    mail_subject,
                    message,
                    settings.EMAIL_HOST_USER,
                    [to_email],
                    fail_silently=True,
                    html_message=message,
                )				
				# return HttpResponse('Please confirm your email address to complete the registration')  
				return	redirect('/confirm-address')

	else:
		form = UserRegisterForm()        

	context = { 'form' : form }
	return render(request, 'register.html', context)

def activate(request, uidb64, token):  
    User = get_user_model()  
    try:  
        uid = force_str(urlsafe_base64_decode(uidb64))  
        user = User.objects.get(pk=uid)  
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):  
        user = None  
    if user is not None and account_activation_token.check_token(user, token):  
        user.is_active = True  
        user.save()
        
        return	redirect('/confirmed-email')  
        #return HttpResponse('Thank you for your email confirmation. Now you can login your account.')  
    else:  
        return	redirect('/invalid-link') 
        # return HttpResponse('Activation link is invalid!') 


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


def professors(request):
	professors = Professor.objects.all()
    
	return render(request,'professors.html', {'professors':professors})

@login_required
def professors_more(request, pk):
	professor = get_object_or_404(Professor, pk = pk)
    
	return render(request,'professprofessors_moreors.html', {'professor':professor})

def confirm_address(request):
    return render(request,'confirm-address.html',)

def confirmed_email(request):
    return render(request,'confirmed-email.html',)

def invalid_link (request):
    return render(request,'invalid-link.html',)