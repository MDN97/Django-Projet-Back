# Generated by Django 5.1.4 on 2024-12-20 13:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MBA_app', '0002_remove_travail_etudiants_etudiant_date_naissance_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='etudiant',
            name='Date_Naissance',
        ),
        migrations.AddField(
            model_name='travail',
            name='etudiants',
            field=models.ManyToManyField(to='MBA_app.etudiant'),
        ),
        migrations.AlterField(
            model_name='etudiant',
            name='Adr_mail',
            field=models.EmailField(max_length=254, verbose_name=''),
        ),
    ]