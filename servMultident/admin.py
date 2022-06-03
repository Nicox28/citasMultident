from django.contrib import admin
from servMultident.models import paciente,usuario,clinica,consultorio, especialidad,cat_per,personal,tratamiento,cita,det_hist,historial


# Register your models here.

class pacienteAdmin(admin.ModelAdmin):
    list_display = ('nomb_pac','apellido_pac','direcc_pac','cel_pac','docu_pac','fecha_nac_pac','sexo_pac')
    search_fields = ('docu_pac',)

class clinicaAdmin(admin.ModelAdmin):
    list_display = ('ruc','direcc_cli','razon')
    search_fields = ('ruc',)

class consultorioAdmin(admin.ModelAdmin):
    list_display = ('num_consult','nom_consult')
    search_fields = ('nom_consult',)

admin.site.register(paciente, pacienteAdmin)
admin.site.register(clinica, clinicaAdmin) 
admin.site.register(consultorio, consultorioAdmin) 
 