from django.urls import include, path

urlpatterns = [
    path('paciente/', include('paciente.urls')),
    path('administrador/', include('administracao.urls')),
    path('instituicao/', include('instituicao.urls')),
    path('fisioterapeuta/', include('fisioterapeuta.urls')),
]
