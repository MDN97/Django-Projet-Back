from django.db import models
from django.db.models.fields import CharField
from django.utils import timezone
from django.utils.timezone import now
from django import forms
from django.db.models import fields
# Create your models here.
class niveau (models.TextChoices):
  premiere=('premiere','1_ère')
  deuxieme=('deuxieme','2_ème')
  troisieme=('troisieme','3_ème')

class type(models.TextChoices):
   Logiciel=('Logiciel','logiciel')
   Materiel=('Materiel','Materiel')

class etatE(models.TextChoices):
    Present=('Present','Present')
    Absent=('Absent','Absent')
    Retard=('Retard','Retard')
    Exclu=('Exclu','Exclu')

class etatS(models.TextChoices):
    En_cours=('En_cours','en cours')
    Termine=('Termine','Terminé')
    Annule=('Annule ','Annulé') 
    Differe=('Differe','Différé')

class typeS(models.TextChoices):
    Normal=('Normale','Normale')
    Rattrapage=('Rattrapage','Rattrapage') 
    Soutien=('Soutien','Soutien')    
    Formation=('Formation','Formation')


class situaion (models.TextChoices):
    Nouveau =('Nouveau','nouveau')
    Redoublant=('Redoublant','Redoublant')
    Derogataire=('Derogataire','Derogataire')
    Autre=('Autre','Autre')


class etatTravail(models.TextChoices):
 valide=('valide','valide')
 non_valide=('non_valide','non_valide')

class typeE(models.TextChoices):
 mp4=('mp4','mp4')
 flv=('flv','flv')
 mov=('mov','mov')
 avi=('avi','avi')
 wmv=('wmv','wmv')

class typeM(models.TextChoices):
    optionnel=('Optionnel','Optionnel')
    obligatoire=('obligatoire','obligatoire')

class Module(models.Model):
    Nom=models.CharField(max_length=20,unique=True)
    Du=models.CharField( max_length=50)
    Type=models.CharField(max_length=20,choices=typeM.choices)
    class Meta:
        db_table='Module'

class Groupe(models.Model):
    Nom=models.CharField(max_length=20)
    Nombre_etud=models.IntegerField()
    ##Email=models.EmailField((""), max_length=254)
    Niveau=models.CharField(max_length=20,choices=niveau.choices)
    modules=models.ManyToManyField(Module,null=True, blank=True)
    class Meta :
        db_table='Groupe'
        


class Etudiant(models.Model):
    Nom = models.CharField(max_length=20)
    Prenom=models.CharField(max_length=20)
    Date_Naissance=models.DateField
    Photo=models.ImageField(null=True,blank=True)
    Adr_mail=models.EmailField((""), max_length=254)
    Etat=models.CharField(max_length=20,choices=etatE.choices,default='Present')
    Situation=models.CharField(max_length=20,choices=situaion.choices,default='Nouveau')

    
    groupe=models.ForeignKey('Groupe',on_delete=models.CASCADE)
   
    class Meta :
        db_table='Etudiant'

     
        
class Absence(models.Model):
    Date=models.DateField
    Motif=models.CharField(max_length=100)
    Justificatif = models.ImageField(null=True, blank=True)
    etudiant=models.ForeignKey('Etudiant',on_delete=models.CASCADE)

    class Meta : 
        db_table='Absence'








class Outil(models.Model):
    Nom=models.CharField(max_length=50)
    Type=models.CharField(max_length=20,choices=type.choices)
    class Meta:
        db_table='Outil'



class Seance (models.Model):
    Heure_deb=models.TimeField((""), auto_now=False, auto_now_add=False)
    Heure_fin=models.TimeField((""), auto_now=False, auto_now_add=False)
    Num_salle=models.CharField( max_length=3)
    Objectif=models.CharField(max_length=100)
    Resume=models.CharField(max_length=100)
    Etat=models.CharField(max_length=20,choices=etatS.choices,default='En_cours')
    Type=models.CharField(max_length=20,choices=typeS.choices,default='Normale')
    Outil_seance=models.ManyToManyField(Outil)
     
    class Meta:
        db_table='Seance'


class Enregistrement(models.Model):
    Nom=models.CharField(max_length=50,unique=True)
    Chemin=models.FileField(null=True)
    Type=models.CharField(max_length=20,choices=typeE.choices,default='mp4')
    niveau=models.CharField(max_length=20,choices=niveau.choices)
    seance=models.ForeignKey(Seance,on_delete=models.CASCADE)

    class Meta:
        db_table='Enregistrement'

class Enseignant(models.Model):
    Nom=models.CharField(max_length=20)
    Prenom=models.CharField(max_length=20)
    Adr_person=models.EmailField( max_length=254)
    Adr_pro=models.EmailField( max_length=254)
    Du = models.CharField(max_length=20, null=True, blank=True)  # Optional field
    Photo=models.ImageField(null=True,blank=True)

    class Meta:
        db_table='Enseignant'




class Ens_Module(models.Model):
    module=models.ForeignKey(Module,on_delete=models.CASCADE)
    enseignant=models.ForeignKey(Enseignant,on_delete=models.CASCADE)
    Ens_Resp=models.IntegerField(name='Ens_Responsable')



class Travail(models.Model):
    Titre=models.CharField(max_length=20)
    Date_Lancement=models.DateField(default=timezone.now)
    Date_limite=models.DateField(default=timezone.now)
    Nature=models.CharField(max_length=20)
    Descriptif=models.CharField(max_length=20)
    Piece_E=models.FileField(null=True)
    Piece_R=models.FileField(null=True)
    Etat=models.CharField(max_length=20,choices=etatTravail.choices,default=('non_valide'))
    Evaluation=models.CharField(max_length=20)
    module=models.ForeignKey('Module',on_delete=models.CASCADE)
    etudiants=models.ManyToManyField(Etudiant)


class EtudiantForm(forms.ModelForm):
    class Meta:
        model=Etudiant
        fields='__all__'
