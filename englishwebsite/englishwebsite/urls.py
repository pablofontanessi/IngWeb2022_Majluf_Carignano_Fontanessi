from django.contrib import admin
from django.urls import path, include
from englishwebsite_app import views
from django.views.generic.base import TemplateView
from django.conf.urls.static import static
from django.conf import settings 
#from englishwebsite_app.views import WrittingExercise_detail

urlpatterns = [
    path('', views.base),
    path('homelogin', views.homelogin),
    path('admin/', admin.site.urls),
    path('writing', views.writing),
    path('reading', views.reading),
    path('listening', views.listening),
    path('speaking', views.speaking),
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
    path('activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/',  
    views.activate, name='activate'),
    #confirm address in register
    path("confirm-address", views.confirm_address),
    #confirmed email
    path("confirmed-email", views.confirmed_email),   
    #invalid link
    path("invalid-link", views.invalid_link),  

    #auth login
    path("accounts/", include("django.contrib.auth.urls")),

    #professors
    path("professors/", views.professors),
    
]

urlpatterns+= static(settings .MEDIA_URL,document_root = settings.MEDIA_ROOT)
