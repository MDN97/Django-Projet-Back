from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.serializers import Serializer
from MBA_app.models import Absence, Enregistrement, Ens_Module, Enseignant, Etudiant, Groupe, Module, Outil, Seance, Travail
from MBA_app.serializers import EnregistrementSerializer, Ens_ModuleSerializer, EnseignantSerializer, EtudiantSerializer,ModuleSerializer,GroupeSerializer,AbsenceSerializer,OutilSerializer, SeanceSerializer, TravailSerializer

# Create your views here.
@api_view(['GET'])
def getAllStudents(request):
    

    if request.method=='GET':
        if Etudiant.objects.count==0:
            return Response(status=status.HTTP_204_NO_CONTENT)
        Etudiants=Etudiant.objects.all()
        result=EtudiantSerializer(Etudiants,many=True)
        return Response(result.data,status=status.HTTP_200_OK)
    return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)

    #get student by Pk
@api_view(['GET']) 
def getByPk(pk):
    try:
        book = Etudiant.objects.get(pk=pk)
    except Etudiant.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    return book



@api_view(['POST'])
def addStudent(request):
    """
    List all code snippets, or create a new snippet.
    """
    

    if request.method == 'POST':
        serializer = EtudiantSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



#Delete with pk
@api_view(['DELETE'])
def deleteStudent(request, pk):
    try:
        student= Etudiant.objects.get(pk=pk)
    except Etudiant.DoesNotExist :
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'DELETE':
        student.delete()
        return Response(status=status.HTTP_200_OK)
    return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)

    #update Student 
@api_view(['PUT','PATCH'])
def UpdateStudent(request,pk):
    try:
        student= Etudiant.objects.get(pk=pk)
    except Etudiant.DoesNotExist :
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method=='PUT':
        studentSerialized = EtudiantSerializer(student,request.data)
    elif request.method=='PATCH':
        studentSerialized = EtudiantSerializer(student,request.data,partial=True)
    else:
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
    if studentSerialized.is_valid():
            studentSerialized.save()
            return Response(status=status.HTTP_201_CREATED)
    return Response(studentSerialized.errors, status=status.HTTP_400_BAD_REQUEST)

    ############################# API_Module ##################################
@api_view(['GET'])
def getAllModules(request):
    

    if request.method=='GET':
        if Module.objects.count==0:
            return Response(status=status.HTTP_204_NO_CONTENT)
        Modules=Module.objects.all()
        result=ModuleSerializer(Modules,many=True)
        return Response(result.data,status=status.HTTP_200_OK)
    return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)

#Ajouter un Module
@api_view(['POST'])
def addModule(request):
    """
    List all code snippets, or create a new snippet.
    """
    

    if request.method == 'POST':
        serializer = ModuleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


#Update Module
@api_view(['PUT','PATCH'])
def UpdateModule(request,pk):
    try:
        student= Module.objects.get(pk=pk)
    except Module.DoesNotExist :
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method=='PUT':
        moduleSerialized = ModuleSerializer(student,request.data)
    elif request.method=='PATCH':
        moduleSerialized = ModuleSerializer(student,request.data,partial=True)
    else:
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
    if moduleSerialized.is_valid():
            moduleSerialized.save()
            return Response(status=status.HTTP_201_CREATED)
    return Response(moduleSerialized.errors, status=status.HTTP_400_BAD_REQUEST)

#Delete Module with pk
@api_view(['DELETE'])
def deleteModule(request, pk):
    try:
        module= Module.objects.get(pk=pk)
    except Module.DoesNotExist :
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'DELETE':
        module.delete()
        return Response(status=status.HTTP_200_OK)
    return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)


    ############################# API_ENSEIGNANT ##################################
# Get all Enseignants
@api_view(['GET'])
def getAllTeachers(request):
    if request.method=='GET':
        if Enseignant.objects.count==0:
            return Response(status=status.HTTP_204_NO_CONTENT)
        Enseignants=Enseignant.objects.all()
        result=EnseignantSerializer(Enseignants,many=True)
        return Response(result.data,status=status.HTTP_200_OK)
    return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)

#Get Enseignant by id

def getTeacherByPk(pk):
    try:
        enseignant = Enseignant.objects.get(pk=pk)
    except Enseignant.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    return enseignant

#ajouter  Enseignant
@api_view(['POST'])
def addTeacher(request):
    """
    List all code snippets, or create a new snippet.
    """
    
#creer Etudiant
    if request.method == 'POST':
        serializer = EnseignantSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


#Modifier Etudiant
@api_view(['PUT','PATCH'])
def UpdateTeacher(request, pk):
    
    try:
        enseignant= Enseignant.objects.get(pk=pk)
    except Enseignant.DoesNotExist :
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method=='PUT':
        enseignantSerialized = EnseignantSerializer(enseignant,request.data)
    elif request.method=='PATCH':
        enseignantSerialized = EtudiantSerializer(enseignant,request.data,partial=True)
    else:
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
    if enseignantSerialized.is_valid():
            enseignantSerialized.save()
            return Response(status=status.HTTP_201_CREATED)
    return Response(enseignantSerialized.errors, status=status.HTTP_400_BAD_REQUEST)



#Delete Enseignant
@api_view(['DELETE'])
def deleteTeacher(request, pk):
    try:
        teacher=Enseignant.objects.get(pk=pk)
    except Enseignant.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'DELETE':
        teacher.delete()
        return Response(status=status.HTTP_200_OK)
    return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)

        ############################# API_Groupe ##################################
# Get all Groupe
@api_view(['GET'])
def getAllGroupe(request):
    if request.method=='GET':
        if Groupe.objects.count==0:
            return Response(status=status.HTTP_204_NO_CONTENT)
        groupe=Groupe.objects.all()
        result=GroupeSerializer(groupe,many=True)
        return Response(result.data,status=status.HTTP_200_OK)
    return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)



#ajouter  Groupe
@api_view(['POST'])
def addGroupe(request):
    """
    List all code snippets, or create a new snippet.
    """
    

    if request.method == 'POST':
        serializer = GroupeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


#Modifier groupe
@api_view(['PUT','PATCH'])
def UpdateGroupe(request, pk):
    
    try:
        groupe= Groupe.objects.get(pk=pk)
    except Groupe.DoesNotExist :
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method=='PUT':
        groupeSerialized = GroupeSerializer(groupe,request.data)
    elif request.method=='PATCH':
        groupeSerialized = GroupeSerializer(groupe,request.data,partial=True)
    else:
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
    if groupeSerialized.is_valid():
            groupeSerialized.save()
            return Response(status=status.HTTP_201_CREATED)
    return Response(groupeSerialized.errors, status=status.HTTP_400_BAD_REQUEST)



#Delete groupe
@api_view(['DELETE'])
def deleteGroupe(request, pk):
    try:
        groupe=Groupe.objects.get(pk=pk)
    except Groupe.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'DELETE':
        groupe.delete()
        return Response(status=status.HTTP_200_OK)
    return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)

    ############################# API_ENSEIGNANT ##################################
# Get all Enseignants
@api_view(['GET'])
def getAllTeachers(request):
    if request.method=='GET':
        if Enseignant.objects.count==0:
            return Response(status=status.HTTP_204_NO_CONTENT)
        Enseignants=Enseignant.objects.all()
        result=EnseignantSerializer(Enseignants,many=True)
        return Response(result.data,status=status.HTTP_200_OK)
    return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)

#Get Enseignant by id

def getTeacherByPk(pk):
    try:
        enseignant = Enseignant.objects.get(pk=pk)
    except Enseignant.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    return enseignant

#ajouter  Enseignant
@api_view(['POST'])
def addTeacher(request):
    """
    List all code snippets, or create a new snippet.
    """
    

    if request.method == 'POST':
        serializer = EnseignantSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


#Modifier Etudiant
@api_view(['PUT','PATCH'])
def UpdateTeacher(request, pk):
    
    try:
        enseignant= Enseignant.objects.get(pk=pk)
    except Enseignant.DoesNotExist :
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method=='PUT':
        enseignantSerialized = EnseignantSerializer(enseignant,request.data)
    elif request.method=='PATCH':
        enseignantSerialized = EtudiantSerializer(enseignant,request.data,partial=True)
    else:
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
    if enseignantSerialized.is_valid():
            enseignantSerialized.save()
            return Response(status=status.HTTP_201_CREATED)
    return Response(enseignantSerialized.errors, status=status.HTTP_400_BAD_REQUEST)



#Delete Enseignant
@api_view(['DELETE'])
def deleteTeacher(request, pk):
    try:
        teacher=Enseignant.objects.get(pk=pk)
    except Enseignant.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'DELETE':
        teacher.delete()
        return Response(status=status.HTTP_200_OK)
    return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)

        ############################# API_Absence ##################################
# Get all Absences
@api_view(['GET'])
def getAllAbsence(request):
    if request.method=='GET':
        if Absence.objects.count==0:
            return Response(status=status.HTTP_204_NO_CONTENT)
        absence=Absence.objects.all()
        result=AbsenceSerializer(absence,many=True)
        return Response(result.data,status=status.HTTP_200_OK)
    return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)



#ajouter  Groupe
@api_view(['POST'])
def addAbsence(request):
    """
    List all code snippets, or create a new snippet.
    """
    

    if request.method == 'POST':
        serializer = AbsenceSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


#Modifier Absence
@api_view(['PUT','PATCH'])
def UpdateAbsence(request, pk):
    
    try:
        absence= Absence.objects.get(pk=pk)
    except Absence.DoesNotExist :
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method=='PUT':
        absenceSerialized = AbsenceSerializer(absence,request.data)
    elif request.method=='PATCH':
        absenceSerialized = AbsenceSerializer(absence,request.data,partial=True)
    else:
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
    if absenceSerialized.is_valid():
            absenceSerialized.save()
            return Response(status=status.HTTP_201_CREATED)
    return Response(absenceSerialized.errors, status=status.HTTP_400_BAD_REQUEST)



#Delete Absence
@api_view(['DELETE'])
def deleteAbsence(request, pk):
    try:
        absence=Absence.objects.get(pk=pk)
    except Absence.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'DELETE':
        absence.delete()
        return Response(status=status.HTTP_200_OK)
    return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)

    ############################# API_Outil ##################################
# Get all Outils
@api_view(['GET'])
def getAllOutil(request):
    if request.method=='GET':
        if Outil.objects.count==0:
            return Response(status=status.HTTP_204_NO_CONTENT)
        outil=Outil.objects.all()
        result=OutilSerializer(outil,many=True)
        return Response(result.data,status=status.HTTP_200_OK)
    return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)



#ajouter  Outil
@api_view(['POST'])
def addOutil(request):
    """
    List all code snippets, or create a new snippet.
    """
    

    if request.method == 'POST':
        serializer = OutilSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


#Modifier Outil
@api_view(['PUT','PATCH'])
def UpdateOutil(request, pk):
    
    try:
        outil= Outil.objects.get(pk=pk)
    except Outil.DoesNotExist :
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method=='PUT':
        outilSerialized = OutilSerializer(outil,request.data)
    elif request.method=='PATCH':
        outilSerialized = OutilSerializer(outil,request.data,partial=True)
    else:
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
    if outilSerialized.is_valid():
            outilSerialized.save()
            return Response(status=status.HTTP_201_CREATED)
    return Response(outilSerialized.errors, status=status.HTTP_400_BAD_REQUEST)



#Delete Outil
@api_view(['DELETE'])
def deleteOutil(request, pk):
    try:
        outil=Outil.objects.get(pk=pk)
    except Outil.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'DELETE':
        outil.delete()
        return Response(status=status.HTTP_200_OK)
    return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)

      ############################# API_Seance ##################################
# Get all Seances
@api_view(['GET'])
def getAllSeance(request):
    if request.method=='GET':
        if Seance.objects.count==0:
            return Response(status=status.HTTP_204_NO_CONTENT)
        seance=Seance.objects.all()
        result=SeanceSerializer(seance,many=True)
        return Response(result.data,status=status.HTTP_200_OK)
    return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)



#ajouter une seance
@api_view(['POST'])
def addSeance(request):
    """
    List all code snippets, or create a new snippet.
    """
    

    if request.method == 'POST':
        serializer = SeanceSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


#Modifier Seance
@api_view(['PUT','PATCH'])
def UpdateSeance(request, pk):
    
    try:
        seance= Seance.objects.get(pk=pk)
    except Seance.DoesNotExist :
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method=='PUT':
        seanceSerialized = SeanceSerializer(seance,request.data)
    elif request.method=='PATCH':
        seanceSerialized = SeanceSerializer(seance,request.data,partial=True)
    else:
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
    if seanceSerialized.is_valid():
            seanceSerialized.save()
            return Response(status=status.HTTP_201_CREATED)
    return Response(seanceSerialized.errors, status=status.HTTP_400_BAD_REQUEST)



#Delete Seance
@api_view(['DELETE'])
def deleteSeance(request, pk):
    try:
        seance=Seance.objects.get(pk=pk)
    except Seance.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'DELETE':
        seance.delete()
        return Response(status=status.HTTP_200_OK)
    return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)

############################# API_Travail ##################################
# Get all Travail
@api_view(['GET'])
def getAllTravail(request):
    if request.method=='GET':
        if Travail.objects.count==0:
            return Response(status=status.HTTP_204_NO_CONTENT)
        travail=Travail.objects.all()
        result=TravailSerializer(travail,many=True)
        return Response(result.data,status=status.HTTP_200_OK)
    return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)



#ajouter un travail
@api_view(['POST'])
def addTravail(request):
    """
    List all code snippets, or create a new snippet.
    """
    

    if request.method == 'POST':
        serializer = TravailSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


#Modifier Travail
@api_view(['PUT','PATCH'])
def UpdateTravail(request, pk):
    
    try:
        travail= Travail.objects.get(pk=pk)
    except Travail.DoesNotExist :
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method=='PUT':
        travailSerialized = TravailSerializer(travail,request.data)
    elif request.method=='PATCH':
        travailSerialized = TravailSerializer(travail,request.data,partial=True)
    else:
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
    if travailSerialized.is_valid():
            travailSerialized.save()
            return Response(status=status.HTTP_201_CREATED)
    return Response(travailSerialized.errors, status=status.HTTP_400_BAD_REQUEST)



#Delete Travail
@api_view(['DELETE'])
def deleteTravail(request, pk):
    try:
        travail=Travail.objects.get(pk=pk)
    except Travail.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'DELETE':
        travail.delete()
        return Response(status=status.HTTP_200_OK)
    return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)

    ############################# API_Ens_Module ##################################
# Get all Travail
@api_view(['GET'])
def getAllEns_Module(request):
    if request.method=='GET':
        if Ens_Module.objects.count==0:
            return Response(status=status.HTTP_204_NO_CONTENT)
        ensmodule=Ens_Module.objects.all()
        result=Ens_ModuleSerializer(ensmodule,many=True)
        return Response(result.data,status=status.HTTP_200_OK)
    return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)



#ajouter un Ens_Module
@api_view(['POST'])
def addEns_Module(request):
    """
    List all code snippets, or create a new snippet.
    """
    

    if request.method == 'POST':
        serializer = Ens_ModuleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


#Modifier Ens_Module
@api_view(['PUT','PATCH'])
def UpdateEns_Module(request, pk):
    
    try:
        ensmodule= Ens_Module.objects.get(pk=pk)
    except Ens_Module.DoesNotExist :
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method=='PUT':
        ensmoduleSerialized = Ens_ModuleSerializer(ensmodule,request.data)
    elif request.method=='PATCH':
        ensmoduleSerialized = Ens_ModuleSerializer(ensmodule,request.data,partial=True)
    else:
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
    if ensmoduleSerialized.is_valid():
            ensmoduleSerialized.save()
            return Response(status=status.HTTP_201_CREATED)
    return Response(ensmoduleSerialized.errors, status=status.HTTP_400_BAD_REQUEST)



#Delete Ens_Module
@api_view(['DELETE'])
def deleteEns_Module(request, pk):
    try:
        ensmodule=Ens_Module.objects.get(pk=pk)
    except Ens_Module.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'DELETE':
        ensmodule.delete()
        return Response(status=status.HTTP_200_OK)
    return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)

##############################API Enregistrement############################
@api_view(['GET'])
def getAllEnregistrement(request):
    

    if request.method=='GET':
        if Enregistrement.objects.count==0:
            return Response(status=status.HTTP_204_NO_CONTENT)
        enregistremnets=Enregistrement.objects.all()
        result=EnregistrementSerializer(enregistremnets,many=True)
        return Response(result.data,status=status.HTTP_200_OK)
    return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)

#get enregistrement by Id
@api_view(['GET']) 
def getByPk(pk):
    try:
        enregistrement = Enregistrement.objects.get(pk=pk)
    except Enregistrement.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    return enregistrement 

@api_view(['POST'])
def addEnregistrement(request):
    """
    List all code snippets, or create a new snippet.
    """
    
#creer Enregistrement
    if request.method == 'POST':
        serializer = EnregistrementSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response( status=status.HTTP_400_BAD_REQUEST)



#Delete with id
@api_view(['DELETE'])
def deleteEnregistrement(request, pk):
    try:
        enregistrement= Enregistrement.objects.get(pk=pk)
    except Etudiant.DoesNotExist :
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'DELETE':
        enregistrement.delete()
        return Response(status=status.HTTP_200_OK)
    return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)

#update
@api_view(['PUT','PATCH'])
def UpdateEnrg(request,pk):
    try:
        enrg= Enregistrement.objects.get(pk=pk)
    except Enregistrement.DoesNotExist :
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method=='PUT':
        EnregistrementSerialized = EnregistrementSerializer(enrg,request.data)
    elif request.method=='PATCH':
        studentSerialized = EnregistrementSerializer(enrg,request.data,partial=True)
    else:
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
    if EnregistrementSerialized.is_valid():
            EnregistrementSerialized.save()
            return Response(status=status.HTTP_201_CREATED)
    return Response(EnregistrementSerialized.errors, status=status.HTTP_400_BAD_REQUEST)






