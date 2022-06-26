from django.db import models

# Create your models here.


class paciente(models.Model):
    nomb_pac = models.CharField(max_length=20)
    apellido_pac = models.CharField(max_length=20)
    direcc_pac = models.CharField(max_length=50)
    cel_pac = models.IntegerField()
    docu_pac = models.IntegerField()
    fecha_nac_pac = models.DateField()
    sexo_pac = models.CharField(max_length=15)

    def __srt__(self):
        return self.nomb_pac


class clinica(models.Model):
    ruc = models.IntegerField()
    direcc_cli = models.CharField(max_length=50)
    razon = models.CharField(max_length=30)

    def __srt__(self):
        return self.razon

class consultorio(models.Model):
    num_consult = models.IntegerField()
    nom_consult = models.CharField(max_length=30)

    def __srt__(self):
        return self.num_consult

class especialidad(models.Model):
    num_espe = models.IntegerField()
    nomb_espe = models.CharField(max_length=40)
    
    def __str__(self):
        return self.nomb_espe

class cat_per(models.Model):
    num_cat_per = models.IntegerField()
    nomb_cat_per = models.CharField(max_length=20)
    
    def __str__(self):
        return self.nomb_cat_per

class personal(models.Model):
    nomb_per = models.CharField(max_length=20)
    apellido_per = models.CharField(max_length=20)
    cel_per = models.IntegerField()
    docu_per = models.IntegerField()
    especialidad = models.CharField(max_length=30)
    cat_per = models.CharField(max_length=30)
    sexo_per = models.CharField(max_length=15)  
    
    def __str__(self):
        return self.nomb_per

class usuario(models.Model):
    login = models.CharField(max_length=20)
    clave = models.CharField(max_length=20)
    nomb = models.CharField(max_length=25)
    apellido = models.CharField(max_length=20)
    perfil = models.CharField(max_length=10)

    def __srt__(self):
        return self.login


class tratamiento(models.Model):
    num_trata = models.IntegerField()
    nomb_trata = models.CharField(max_length=20)
    
    def __srt__(self):
        return self.nomb_trata

class cita(models.Model):
    hora = models.TimeField()
    fecha = models.DateField()
    paciente = models.ForeignKey(paciente, on_delete=models.CASCADE)
    personal = models.ForeignKey(personal, on_delete=models.CASCADE)
    consultorio = models.ForeignKey(consultorio, on_delete=models.CASCADE)
    #def __srt__(self):
     #   return self.fecha

class det_hist(models.Model):
    fecha_his = models.DateField
    tratamiento = models.ForeignKey(tratamiento, on_delete=models.CASCADE)

    #def __srt__(self):
     #   return self.fecha_his

class historial(models.Model):
    paciente = models.ForeignKey(paciente, on_delete=models.CASCADE)
    det_hist = models.ForeignKey(det_hist, on_delete=models.CASCADE)

    #def __srt__(self):
     #   return self.det_hist




