from django.contrib import admin
from django.urls import path, include
from englishwebsite_app import views
from django.views.generic.base import TemplateView

urlpatterns = [
    path('', views.base),
    path('homelogin', views.homelogin),
    path('admin/', admin.site.urls),
    
    #user register
    path('register/', views.register), 

    #auth login
    path("accounts/", include("django.contrib.auth.urls")),
]
