"""citasMultident URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path

from rest_framework import routers, permissions
from servMultident import views as viewsCitas

from rest_framework_simplejwt import views as jwt_views


router = routers.DefaultRouter()

router.register(r'paciente', viewsCitas.pacienteViewSet)
router.register(r'clinica', viewsCitas.clinicaViewSet)
router.register(r'consultorio', viewsCitas.consultorioViewSet)
router.register(r'especialidad', viewsCitas.especialidadViewSet)
router.register(r'cat_per', viewsCitas.cat_perViewSet)
router.register(r'personal', viewsCitas.personalViewSet)
router.register(r'usuario', viewsCitas.usuarioViewSet)
router.register(r'Tratamiento', viewsCitas.tratamientoViewSet)
router.register(r'cita', viewsCitas.citaViewSet)
router.register(r'rec_tratamiento', viewsCitas.rec_tratamientoViewSet)
router.register(r'enfermedad', viewsCitas.enfermedadViewSet)
router.register(r'examen_oral', viewsCitas.examen_oralViewSet)
router.register(r'historial', viewsCitas.historialViewSet)

#agregar todos

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('admin/', admin.site.urls),


    path('api/token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
]
