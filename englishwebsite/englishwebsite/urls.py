from django.contrib import admin
from django.urls import path, include
from englishwebsite_app import views
from django.views.generic.base import TemplateView
from django.conf.urls.static import static
from django.conf import settings 
from englishwebsite_app.views import *
from django.conf import settings

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
    #path('writting',writingView.as_view(), name= 'writting' ),
    path('exerciseDetail/<int:id>',views.exerciseDetail, name= 'exercise-detail' ),
    path('addQuestion/', views.addQuestion,name='addQuestion'),
    path('MultipleOption/', views.MultipleOpcList,name='MultipleOption'),
    path('MultipleOption/<int:id>', views.MultipleQuestionsExercises,name='MultipleQuestionsExercises'),
    
    #search
    path('search/', include('haystack.urls')),

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
    path("professors_more/", views.professors_more),
    path("professors_more/<int:id>", views.professors_more, name="professors_more"),
    path("professors/professors_apply", views.professors_apply),

    #robots
    path(
        "robots.txt",
        TemplateView.as_view(template_name="robots.txt", content_type="text/plain"),
    ),
]

urlpatterns+= static(settings .MEDIA_URL,document_root = settings.MEDIA_ROOT)
