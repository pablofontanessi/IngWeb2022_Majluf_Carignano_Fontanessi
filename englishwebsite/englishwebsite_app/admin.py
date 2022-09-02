from unicodedata import category
from django.contrib import admin
from englishwebsite_app.models import Exercise_Category, Post, User


@admin.register(User)
class AdminUser(admin.ModelAdmin):
    user_name = ('id', 'nombre')

admin.site.register(Exercise_Category)
admin.site.register(Post)