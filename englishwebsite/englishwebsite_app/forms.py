from asyncore import file_dispatcher
from dataclasses import fields
from django import forms
from django.forms import ModelForm, ModelChoiceField
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import *



class UserRegisterForm(UserCreationForm):
	username = forms.CharField(label='Username')
	email = forms.EmailField()
	password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
	password2 = forms.CharField(label='Confirma Contraseña', widget=forms.PasswordInput)

	class Meta:
		model = User
		fields = ['username', 'email', 'password1', 'password2']
		help_texts = {k:"" for k in fields }

class CreateNewExercise(ModelForm):
	title_exercise = forms.CharField(max_length= 250)
	description_exercise = forms.CharField(max_length= 500)
	activity = forms.CharField(max_length= 500,widget=forms.Textarea)
	correct_answer = forms.CharField(max_length= 500,widget=forms.Textarea)
	#author = forms.TypedChoiceField(queryset=User.objects.filter(username =User.username), empty_label=None)
	category = forms.ModelChoiceField(queryset=Exercise_Category.objects.all(), empty_label=None)
	file = forms.FileField(required=False)


	class Meta:
		model= Post
		fields=['title_exercise','description_exercise','activity','correct_answer','category','file' ]

class addQuestionform(ModelForm):
    class Meta:
        model=QuesModel
        fields="__all__"