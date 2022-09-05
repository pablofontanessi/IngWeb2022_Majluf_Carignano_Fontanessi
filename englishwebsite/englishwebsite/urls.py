from django.contrib import admin
from django.urls import path, include
from englishwebsite_app import views
from django.views.generic.base import TemplateView
#from englishwebsite_app.views import WrittingExercise_detail

urlpatterns = [
    path('', views.base),
    path('homelogin', views.homelogin),
    path('admin/', admin.site.urls),
    path('writing', views.writing),
    path('reading', views.reading),
    path('listening', views.listening),
    path('grammar-exercises', views.grammarExercices),
    path('alphabet-exercises',views.alphabetExercises),
    path('articles-exercises',views.articlesExercises),
    path('vocabulary-exercises',views.vocabularyExercises),
    path('countries-nationalitiesAtoC',views.nacionalitiesExercisesAtoC),
    path('countries-nationalitiesC-H',views.nacionalitiesExercisesCtoH),
    path('createExercises',views.create_exercise),
    #path('writing/exercises/<int:pk>',WrittingExercise_detail.as_view(), name= 'exercise-detail' ),


    #user register
    path('register/', views.register), 

    #auth login
    path("accounts/", include("django.contrib.auth.urls")),
]
