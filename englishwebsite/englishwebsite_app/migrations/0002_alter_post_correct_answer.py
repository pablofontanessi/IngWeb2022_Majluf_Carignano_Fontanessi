# Generated by Django 4.1 on 2022-09-02 18:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('englishwebsite_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='correct_answer',
            field=models.TextField(blank=True, max_length=500, verbose_name='Correct answer'),
        ),
    ]
