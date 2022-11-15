from django.shortcuts import render
from servMultident.models import paciente,clinica,consultorio, especialidad,cat_per,personal,usuario,tratamiento,cita,rec_tratamiento,historial,enfermedad,examen_oral
from servMultident.serializer import pacienteSerializer,clinicaSerializer,consultorioSerializer,especialidadSerializer,cat_perSerializer,personalSerializer,usuarioSerializer,tratamientoSerializer,citaSerializer,rec_tratamientoSerializer,historialSerializer,enfermedadSerializer,examen_oralSerializer
from rest_framework import permissions, viewsets, filters
# Create your views here.

class pacienteViewSet(viewsets.ModelViewSet):
    queryset = paciente.objects.all().order_by('-id')
    serializer_class = pacienteSerializer
    permission_classes = [permissions.IsAuthenticated]    
    filter_backends = [filters.SearchFilter]
    search_fields = ['=id']

class clinicaViewSet(viewsets.ModelViewSet):
    queryset = clinica.objects.all()
    serializer_class = clinicaSerializer
    permission_classes = [permissions.IsAuthenticated]    
    filter_backends = [filters.SearchFilter]
    search_fields = ['=id']

class consultorioViewSet(viewsets.ModelViewSet):
    queryset = consultorio.objects.all()
    serializer_class = consultorioSerializer
    permission_classes = [permissions.IsAuthenticated]    
    filter_backends = [filters.SearchFilter]
    search_fields = ['=id']

class especialidadViewSet(viewsets.ModelViewSet):
    queryset = especialidad.objects.all()
    serializer_class = especialidadSerializer
    permission_classes = [permissions.IsAuthenticated]    
    filter_backends = [filters.SearchFilter]
    search_fields = ['=id']

class cat_perViewSet(viewsets.ModelViewSet):
    queryset = cat_per.objects.all()
    serializer_class = cat_perSerializer
    permission_classes = [permissions.IsAuthenticated]    
    filter_backends = [filters.SearchFilter]
    search_fields = ['=id']

class personalViewSet(viewsets.ModelViewSet):
    queryset = personal.objects.all()
    serializer_class = personalSerializer
    permission_classes = [permissions.IsAuthenticated]    
    filter_backends = [filters.SearchFilter]
    search_fields = ['=id']

class usuarioViewSet(viewsets.ModelViewSet):
    queryset = usuario.objects.all()
    serializer_class = usuarioSerializer
    permission_classes = [permissions.IsAuthenticated]    
    filter_backends = [filters.SearchFilter]
    search_fields = ['=login']

class tratamientoViewSet(viewsets.ModelViewSet):
    queryset = tratamiento.objects.all()
    serializer_class = tratamientoSerializer
    permission_classes = [permissions.IsAuthenticated]    
    filter_backends = [filters.SearchFilter]
    search_fields = ['=id']

class citaViewSet(viewsets.ModelViewSet):
    queryset = cita.objects.all()
    serializer_class = citaSerializer
    permission_classes = [permissions.IsAuthenticated]    
    filter_backends = [filters.SearchFilter]
    search_fields = ['=id']

class rec_tratamientoViewSet(viewsets.ModelViewSet):
    queryset = rec_tratamiento.objects.all()
    serializer_class = rec_tratamientoSerializer
    permission_classes = [permissions.IsAuthenticated]    
    filter_backends = [filters.SearchFilter]
    search_fields = ['=id']


class enfermedadViewSet(viewsets.ModelViewSet):
    queryset = enfermedad.objects.all()
    serializer_class = enfermedadSerializer
    permission_classes = [permissions.IsAuthenticated]    
    filter_backends = [filters.SearchFilter]
    search_fields = ['=id']


class examen_oralViewSet(viewsets.ModelViewSet):
    queryset = examen_oral.objects.all()
    serializer_class = examen_oralSerializer
    permission_classes = [permissions.IsAuthenticated]    
    filter_backends = [filters.SearchFilter]
    search_fields = ['=id']

class historialViewSet(viewsets.ModelViewSet):
    queryset = historial.objects.all()
    serializer_class = historialSerializer
    permission_classes = [permissions.IsAuthenticated]    
    filter_backends = [filters.SearchFilter]
    search_fields = ['=id']