from django.contrib.auth.models import User, Group
from servMultident.models import paciente,clinica,consultorio, especialidad,cat_per,personal,usuario,tratamiento,cita,det_hist,historial
from rest_framework import serializers


class pacienteSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = paciente
        fields = '__all__'

class clinicaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = clinica
        fields = '__all__'

class consultorioSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = consultorio
        fields = '__all__'

class especialidadSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = especialidad
        fields = '__all__'

class cat_perSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = cat_per
        fields = '__all__'

class personalSerializer(serializers.HyperlinkedModelSerializer):
    datosEspecialidad = especialidadSerializer(source = "especialidad", read_only=True)
    class Meta:
        model = personal
        fields = '__all__'

class usuarioSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = usuario
        fields = '__all__'

class tratamientoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = tratamiento
        fields = '__all__'

class citaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = cita
        fields = '__all__'

class det_histSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = det_hist
        fields = '__all__'

class historialSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = historial
        fields = '__all__'

