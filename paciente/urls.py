from . import views
from django.urls import path
from rest_framework.routers import DefaultRouter
from formularios.views import FormulariosPorPacienteView

router = DefaultRouter()
router.register(r'', views.PacienteViewSet, basename='Paciente')
urlpatterns = [

    path('<int:paciente_id>/formularios/', FormulariosPorPacienteView.as_view(), name='formulariosdepaciente'),

]
urlpatterns += router.urls
