"""MBA URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.conf import  settings
from django.conf.urls.static import static
from MBA_app.serializers import SeanceSerializer
from rest_framework import routers
from MBA_app.views import UpdateAbsence, UpdateEnrg, UpdateEns_Module, UpdateGroupe, UpdateModule, UpdateOutil, UpdateSeance, UpdateStudent, UpdateTeacher, UpdateTravail, addAbsence, addEnregistrement, addEns_Module, addGroupe, addModule, addOutil, addSeance, addStudent, addTeacher, addTravail, deleteAbsence, deleteEnregistrement, deleteEns_Module, deleteGroupe, deleteModule, deleteOutil, deleteSeance, deleteStudent, deleteTeacher, deleteTravail, getAllAbsence, getAllEnregistrement, getAllEns_Module, getAllGroupe, getAllModules, getAllOutil, getAllSeance, getAllStudents, getAllTeachers, getAllTravail, getByPk, getTeacherByPk


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path(r'Etudiant/all/',getAllStudents,name='allEtudiant'),
    path(r'Etudiant/getbyid/<int:pk>',getByPk,name="studID"),
    path(r'Etudiant/add/',addStudent,name='addEtudiant'),
    path(r'Etudiant/delete/<int:pk>',deleteStudent),
    path(r'Etudiant/update/<int:pk>',UpdateStudent),

    path(r'Module/getAllModules/',getAllModules),
    path(r'Module/addModule/',addModule),
    path(r'Module/deleteM/<int:pk>',deleteModule),
    path(r'Module/updateM/<int:pk>',UpdateModule),

    path(r'Enseignant/all/',getAllTeachers,name='allTeacher'),
    path(r'Enseignant/getbyid/<int:pk>',getTeacherByPk,name="TeacherID"),
    path(r'Enseignant/add/',addTeacher,name='addEnseignant'),
    path(r'Enseignant/delete/<int:pk>',deleteTeacher),
    path(r'Enseignant/update/<int:pk>',UpdateTeacher),

    path(r'Groupe/all/',getAllGroupe,name='allGroupes'),
    path(r'Groupe/add/',addGroupe,name='addGroupe'),
    path(r'Groupe/delete/<int:pk>',deleteGroupe),
    path(r'Groupe/update/<int:pk>',UpdateGroupe),

    path(r'Absence/all/',getAllAbsence,name='allAbsences'),
    path(r'Absence/add/',addAbsence,name='addAbsence'),
    path(r'Absence/delete/<int:pk>',deleteAbsence),
    path(r'Absence/update/<int:pk>',UpdateAbsence),

    path(r'Outil/all/',getAllOutil,name='allOutil'),
    path(r'Outil/add/',addOutil,name='addEnseignant'),
    path(r'Outil/delete/<int:pk>',deleteOutil),
    path(r'Outil/update/<int:pk>',UpdateOutil),

    path(r'Seance/all/',getAllSeance,name='allSeances'),
    path(r'Seance/add/',addSeance,name='addSeance'),
    path(r'Seance/delete/<int:pk>',deleteSeance),
    path(r'Seance/update/<int:pk>',UpdateSeance),
    
    path(r'Travail/all/',getAllTravail,name='allTravail'),
    path(r'Travail/add/',addTravail,name='addTravail'),
    path(r'Travail/delete/<int:pk>',deleteTravail),
    path(r'Travail/update/<int:pk>',UpdateTravail),
        
    path(r'Ens_Module/all/',getAllEns_Module,name='allEns_Module'),
    path(r'Ens_Module/add/',addEns_Module,name='addEns_Module'),
    path(r'Ens_Module/delete/<int:pk>',deleteEns_Module),
    path(r'Ens_Module/update/<int:pk>',UpdateEns_Module),

    path(r'Enregistrement/all/',getAllEnregistrement,name='allEnregistrement'), 
    path(r'Enregistrement/add/',addEnregistrement,name='addEnseignant'),
    path(r'Enregistrement/delete/<int:pk>',deleteEnregistrement),
    path(r'Enregistrement/update/<int:pk>',UpdateEnrg)
   
]
