from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Exercise_Category(models.Model):
    id = models.AutoField(primary_key=True)
    name_category = models.CharField('Category name', max_length=100, blank= False, null=False)

    class Meta: 
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name_category


class Post(models.Model):
    id = models.AutoField(primary_key=True)
    title_exercise = models.CharField('Title', max_length= 250, blank= False, null=False)
    #slug = models.CharField('Slug', max_length= 100, blank= False, null= False)
    description_exercise = models.CharField('Description', max_length= 500, blank= False, null=False)
    activity = models.TextField('Activity',blank=False, max_length= 500)
    correct_answer = models.TextField('Correct answer',blank=True, max_length= 500)
    file = models.FileField(upload_to='uploads')
    #author = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Exercise_Category, on_delete=models.CASCADE)
    available = models.BooleanField('Published/No Published', default= True)
    creation_date = models.DateField('Creation date', auto_now= False, auto_now_add= True)

    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'

    def __str__(self):
        return self.title_exercise
        

class Professor(models.Model):
    user = models.OneToOneField(User, on_delete= models.CASCADE)
    id = models.AutoField(primary_key = True)
    name = models.CharField('Name', max_length= 250, blank=False, null=False)
    short_description = models.CharField('Short description', max_length= 100, blank= False, null=False)
    full_description = models.CharField('Full description', max_length= 500, blank= False, null=False)
    avatar = models.ImageField()

    class Meta:
        verbose_name = 'Professor'
        verbose_name_plural = 'Professors'

    def __str__(self):
        return self.user.username