from unicodedata import category
from xml.etree.ElementTree import Comment
from django.contrib import admin
from django.contrib.auth.models import User
from englishwebsite_app.models import Exercise_Category, Post, Professor, Comment


admin.register(User)
admin.site.register(Exercise_Category)
admin.site.register(Post)
admin.site.register(Professor)
admin.site.register(Comment)