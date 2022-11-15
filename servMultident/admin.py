from django.contrib import admin
from servMultident.models import paciente,clinica,consultorio, especialidad,cat_per,personal,usuario,tratamiento,cita,rec_tratamiento,historial,enfermedad,examen_oral


# Register your models here.

class pacienteAdmin(admin.ModelAdmin):
    list_display = ('nomb_pac','apellido_pac','direcc_pac','cel_pac','docu_pac','fecha_nac_pac','sexo_pac')
    search_fields = ('nomb_pac',)

class clinicaAdmin(admin.ModelAdmin):
    list_display = ('ruc','direcc_cli','razon')
    search_fields = ('razon',)

class consultorioAdmin(admin.ModelAdmin):
    list_display = ('num_consult','nom_consult')
    search_fields = ('num_consult',)

class especialidadAdmin(admin.ModelAdmin):
    list_display = ('num_espe','nomb_espe')
    search_fields = ('nomb_espe',)

class cat_perAdmin(admin.ModelAdmin):
    list_display = ('num_cat_per','nomb_cat_per')
    search_fields = ('nomb_cat_per',)

class personalAdmin(admin.ModelAdmin):
    list_display = ('nomb_per','apellido_per','cel_per','docu_per','especialidad','cat_per','sexo_per')
    search_fields = ('nomb_per',)

class usuarioAdmin(admin.ModelAdmin):
    list_display = ('login','clave','nomb','apellido','perfil')
    search_fields = ('login',)

class tratamientoAdmin(admin.ModelAdmin):
    list_display = ('num_trata','nomb_trata')
    search_fields = ('nomb_trata',)

class citaAdmin(admin.ModelAdmin):
    list_display = ('hora','fecha','nombre_c','apellido_c','correo')
    search_fields = ('fecha',)

class rec_tratamientoAdmin(admin.ModelAdmin):
    list_display = ('fecha_tratami','tratamiento','personal','estado','paciente')
    search_fields = ('estado',)

class enfermedadAdmin(admin.ModelAdmin):
    list_display = ('num_enfer','nomb_enfer')
    search_fields = ('nomb_enfer',)

class examen_oralAdmin(admin.ModelAdmin):
    list_display = ('impresionGe','cabeza','cuello','mejillas','lengua','piso_boca','pilares_pala','encias')
    search_fields = ('impresionGe',)

class historialAdmin(admin.ModelAdmin):
    list_display = ('paciente','rec_tratamiento','examen_oral','enfermedad','fecha_histo','contactar','cel_contac','alergia','toma_medica','frecuencia_visi','experiencia_trauma','extraccion_mue','sangre_enci','estetica_dental','motivo_consul','presion_art','talla','peso')
    search_fields = ('paciente',)

admin.site.register(paciente, pacienteAdmin)
admin.site.register(clinica, clinicaAdmin) 
admin.site.register(consultorio, consultorioAdmin) 
admin.site.register(especialidad, especialidadAdmin)
admin.site.register(cat_per, cat_perAdmin) 
admin.site.register(personal, personalAdmin) 
admin.site.register(usuario, usuarioAdmin) 
admin.site.register(tratamiento, tratamientoAdmin)
admin.site.register(cita, citaAdmin)  
admin.site.register(rec_tratamiento, rec_tratamientoAdmin)
admin.site.register(enfermedad, enfermedadAdmin)
admin.site.register(examen_oral, examen_oralAdmin)
admin.site.register(historial, historialAdmin) 
