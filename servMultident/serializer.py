from django.contrib.auth.models import User, Group
from servMultident.models import paciente,clinica,consultorio, especialidad,cat_per,personal,usuario,tratamiento,cita,rec_tratamiento,historial,enfermedad,examen_oral
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

class rec_tratamientoSerializer(serializers.HyperlinkedModelSerializer):
    datosPersonal = personalSerializer(source = "personal", read_only=True)
    datosTratamiento = tratamientoSerializer(source = "tratamiento", read_only=True)
    datosPaciente = tratamientoSerializer(source = "paciente", read_only=True)
    class Meta:
        model = rec_tratamiento
        fields = '__all__'

class enfermedadSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = enfermedad
        fields = '__all__'



class examen_oralSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = examen_oral
        fields = '__all__'



class historialSerializer(serializers.HyperlinkedModelSerializer):
    datosPaciente = pacienteSerializer(source = "paciente", read_only=True)
    datosRec_tratamiento = rec_tratamientoSerializer(source = "rec_tratamiento", read_only=True)
    datosEnfermedades = enfermedadSerializer(source = "enfermedad", read_only=True)
    datosExamen_oral = examen_oralSerializer(source = "examen_oral", read_only=True)
    class Meta:
        model = historial
        fields = '__all__'



