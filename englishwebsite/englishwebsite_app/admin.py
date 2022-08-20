from django.contrib import admin
from englishwebsite_app.models import User


@admin.register(User)
class AdminUser(admin.ModelAdmin):
    user_name = ('id', 'nombre')