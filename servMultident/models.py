from django.db import models

# Create your models here.


class paciente(models.Model):
    nomb_pac = models.CharField(max_length=20)
    apellido_pac = models.CharField(max_length=20)
    direcc_pac = models.CharField(max_length=50)
    cel_pac = models.CharField(max_length=9)
    docu_pac = models.CharField(max_length=13)
    fecha_nac_pac = models.DateField()
    sexo_pac = models.CharField(max_length=10)

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
    cel_per = models.CharField(max_length=9)
    docu_per = models.CharField(max_length=13)
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
    nombre_c = models.CharField(max_length=20)
    apellido_c = models.CharField(max_length=20)
    correo = models.CharField(max_length=20)
    
    def __srt__(self):
        return self.nombre_c

class rec_tratamiento(models.Model):
    fecha_tratami = models.DateField()
    tratamiento = models.ForeignKey(tratamiento, on_delete=models.CASCADE)
    personal = models.ForeignKey(personal, on_delete=models.CASCADE)
    estado = models.CharField(max_length=5)
    paciente = models.ForeignKey(paciente, on_delete=models.CASCADE)

    def __srt__(self):
        return self.estado

class enfermedad(models.Model):
    num_enfer = models.IntegerField()
    nomb_enfer = models.CharField(max_length=20)
    
    def __srt__(self):
        return self.nomb_enfer

class examen_oral(models.Model):
    impresionGe = models.CharField(max_length=40)
    cabeza = models.CharField(max_length=40)
    cuello = models.CharField(max_length=40)
    mejillas = models.CharField(max_length=40)
    lengua = models.CharField(max_length=20)
    piso_boca = models.CharField(max_length=20)
    pilares_pala = models.CharField(max_length=40)
    encias = models.CharField(max_length=40)
    
    def __srt__(self):
        return self.impresionGe

class historial(models.Model):
    paciente = models.ForeignKey(paciente, on_delete=models.CASCADE)
    rec_tratamiento = models.ForeignKey(rec_tratamiento, on_delete=models.CASCADE)
    examen_oral = models.ForeignKey(examen_oral, on_delete=models.CASCADE)
    enfermedad = models.ForeignKey(enfermedad, on_delete=models.CASCADE)
    fecha_histo = models.DateField()
    contactar = models.CharField(max_length=40)
    cel_contac = models.CharField(max_length=40)
    alergia = models.CharField(max_length=40)
    toma_medica = models.CharField(max_length=40)
    frecuencia_visi = models.CharField(max_length=40)
    experiencia_trauma = models.CharField(max_length=40)
    extraccion_mue = models.CharField(max_length=40)
    sangre_enci = models.CharField(max_length=40)
    estetica_dental = models.CharField(max_length=40)
    motivo_consul = models.CharField(max_length=40)
    presion_art = models.CharField(max_length=20)
    talla = models.CharField(max_length=20)
    peso = models.CharField(max_length=20)


    def __srt__(self):
        return self.contactar


