# Generated by Django 5.1.4 on 2024-12-20 13:27

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Enseignant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nom', models.CharField(max_length=20)),
                ('Prenom', models.CharField(max_length=20)),
                ('Adr_person', models.EmailField(max_length=254)),
                ('Adr_pro', models.EmailField(max_length=254)),
                ('Du', models.CharField(max_length=20)),
                ('Photo', models.ImageField(blank=True, null=True, upload_to='')),
            ],
            options={
                'db_table': 'Enseignant',
            },
        ),
        migrations.CreateModel(
            name='Etudiant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nom', models.CharField(max_length=20)),
                ('Prenom', models.CharField(max_length=20)),
                ('Photo', models.ImageField(blank=True, null=True, upload_to='')),
                ('Adr_mail', models.EmailField(max_length=254, verbose_name='')),
                ('Etat', models.CharField(choices=[('Present', 'Present'), ('Absent', 'Absent'), ('Retard', 'Retard'), ('Exclu', 'Exclu')], default='Present', max_length=20)),
                ('Situation', models.CharField(choices=[('Nouveau', 'nouveau'), ('Redoublant', 'Redoublant'), ('Derogataire', 'Derogataire'), ('Autre', 'Autre')], default='Nouveau', max_length=20)),
            ],
            options={
                'db_table': 'Etudiant',
            },
        ),
        migrations.CreateModel(
            name='Groupe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nom', models.CharField(max_length=20)),
                ('Nombre_etud', models.IntegerField()),
                ('Niveau', models.CharField(choices=[('premiere', '1_ère'), ('deuxieme', '2_ème'), ('troisieme', '3_ème')], max_length=20)),
            ],
            options={
                'db_table': 'Groupe',
            },
        ),
        migrations.CreateModel(
            name='Module',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nom', models.CharField(max_length=20, unique=True)),
                ('Du', models.CharField(max_length=50)),
                ('Type', models.CharField(choices=[('Optionnel', 'Optionnel'), ('obligatoire', 'obligatoire')], max_length=20)),
            ],
            options={
                'db_table': 'Module',
            },
        ),
        migrations.CreateModel(
            name='Outil',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nom', models.CharField(max_length=50)),
                ('Type', models.CharField(choices=[('Logiciel', 'logiciel'), ('Materiel', 'Materiel')], max_length=20)),
            ],
            options={
                'db_table': 'Outil',
            },
        ),
        migrations.CreateModel(
            name='Absence',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Motif', models.CharField(max_length=100)),
                ('Justificatif', models.ImageField(upload_to='')),
                ('etudiant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='MBA_app.etudiant')),
            ],
            options={
                'db_table': 'Absence',
            },
        ),
        migrations.AddField(
            model_name='etudiant',
            name='groupe',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='MBA_app.groupe'),
        ),
        migrations.AddField(
            model_name='groupe',
            name='modules',
            field=models.ManyToManyField(blank=True, null=True, to='MBA_app.module'),
        ),
        migrations.CreateModel(
            name='Ens_Module',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Ens_Responsable', models.IntegerField()),
                ('enseignant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='MBA_app.enseignant')),
                ('module', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='MBA_app.module')),
            ],
        ),
        migrations.CreateModel(
            name='Seance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Heure_deb', models.TimeField(verbose_name='')),
                ('Heure_fin', models.TimeField(verbose_name='')),
                ('Num_salle', models.CharField(max_length=3)),
                ('Objectif', models.CharField(max_length=100)),
                ('Resume', models.CharField(max_length=100)),
                ('Etat', models.CharField(choices=[('En_cours', 'en cours'), ('Termine', 'Terminé'), ('Annule ', 'Annulé'), ('Differe', 'Différé')], default='En_cours', max_length=20)),
                ('Type', models.CharField(choices=[('Normale', 'Normale'), ('Rattrapage', 'Rattrapage'), ('Soutien', 'Soutien'), ('Formation', 'Formation')], default='Normale', max_length=20)),
                ('Outil_seance', models.ManyToManyField(to='MBA_app.outil')),
            ],
            options={
                'db_table': 'Seance',
            },
        ),
        migrations.CreateModel(
            name='Enregistrement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nom', models.CharField(max_length=50, unique=True)),
                ('Chemin', models.FileField(null=True, upload_to='')),
                ('Type', models.CharField(choices=[('mp4', 'mp4'), ('flv', 'flv'), ('mov', 'mov'), ('avi', 'avi'), ('wmv', 'wmv')], default='mp4', max_length=20)),
                ('niveau', models.CharField(choices=[('premiere', '1_ère'), ('deuxieme', '2_ème'), ('troisieme', '3_ème')], max_length=20)),
                ('seance', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='MBA_app.seance')),
            ],
            options={
                'db_table': 'Enregistrement',
            },
        ),
        migrations.CreateModel(
            name='Travail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Titre', models.CharField(max_length=20)),
                ('Date_Lancement', models.DateField(default=django.utils.timezone.now)),
                ('Date_limite', models.DateField(default=django.utils.timezone.now)),
                ('Nature', models.CharField(max_length=20)),
                ('Descriptif', models.CharField(max_length=20)),
                ('Piece_E', models.FileField(null=True, upload_to='')),
                ('Piece_R', models.FileField(null=True, upload_to='')),
                ('Etat', models.CharField(choices=[('valide', 'valide'), ('non_valide', 'non_valide')], default='non_valide', max_length=20)),
                ('Evaluation', models.CharField(max_length=20)),
                ('etudiants', models.ManyToManyField(to='MBA_app.etudiant')),
                ('module', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='MBA_app.module')),
            ],
        ),
    ]
