from django.db.models import fields
from rest_framework import serializers
from .models import Absence, Enregistrement, Ens_Module, Enseignant, Etudiant, Groupe, Module, Outil, Seance, Travail

class EtudiantSerializer(serializers.ModelSerializer):
    class Meta :
        model = Etudiant
        fields='__all__'
class ModuleSerializer(serializers.ModelSerializer):
    class Meta :
        model=Module
        fields='__all__'
class GroupeSerializer(serializers.ModelSerializer):
    class Meta :
        model =Groupe
        fields='__all__'
        

class AbsenceSerializer(serializers.ModelSerializer):
    class Meta :
        model = Absence
        fields='__all__'

class OutilSerializer(serializers.ModelSerializer):
    class Meta :
        model = Outil
        fields='__all__'

class SeanceSerializer(serializers.ModelSerializer):
    class Meta :
        model = Seance
        fields='__all__'

class EnregistrementSerializer(serializers.ModelSerializer):
    class Meta :
        model = Enregistrement
        fields='__all__'

class EnseignantSerializer(serializers.ModelSerializer):
    class Meta :
        model = Enseignant
        fields='__all__' 

class   Ens_ModuleSerializer(serializers.ModelSerializer):
    class Meta :
        model =Ens_Module
        fields='__all__'
class   TravailSerializer(serializers.ModelSerializer):
    class Meta :
        model =Travail
        fields='__all__'