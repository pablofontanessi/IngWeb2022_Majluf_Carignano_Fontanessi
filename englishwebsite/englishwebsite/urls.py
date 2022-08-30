from django.contrib import admin
from django.urls import path, include
from englishwebsite_app import views
from django.views.generic.base import TemplateView

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
    
    #user register
    path('register/', views.register), 

    #auth login
    path("accounts/", include("django.contrib.auth.urls")),
]
