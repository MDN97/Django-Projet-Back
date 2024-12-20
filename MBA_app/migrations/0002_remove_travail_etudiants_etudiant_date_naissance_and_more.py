# Generated by Django 5.1.4 on 2024-12-20 13:49

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MBA_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='travail',
            name='etudiants',
        ),
        migrations.AddField(
            model_name='etudiant',
            name='Date_Naissance',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='etudiant',
            name='Adr_mail',
            field=models.EmailField(max_length=254),
        ),
    ]
