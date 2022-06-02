from django.db import models

# Create your models here.

class usuario(models.model):
    login = models.CharField(max_length=20)
    clave = models.CharField(max_length=20)
    id_paciente = models.CharField(max_length=20)
    nomb = models.CharField(max_length=25)
    apellido = models.CharField(max_length=20)

def_srt_(self):
    return self.login
    
# models.DateField(null=true)
# models.integerfield




