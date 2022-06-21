from django.contrib import admin
from servMultident.models import paciente,clinica,consultorio, especialidad,cat_per,personal,usuario,tratamiento,cita,det_hist,historial


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
    list_display = ('login','clave','personal','nomb','apellido','perfil')
    search_fields = ('login',)

class tratamientoAdmin(admin.ModelAdmin):
    list_display = ('num_trata','nomb_trata')
    search_fields = ('nomb_trata',)

class citaAdmin(admin.ModelAdmin):
    list_display = ('hora','fecha','paciente','personal','consultorio')
    search_fields = ('fecha',)

class det_histAdmin(admin.ModelAdmin):
    list_display = ('fecha_his','tratamiento')
    search_fields = ('fecha_his',)

class historialAdmin(admin.ModelAdmin):
    list_display = ('paciente','det_hist')
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
admin.site.register(det_hist, det_histAdmin) 
admin.site.register(historial, historialAdmin) 
