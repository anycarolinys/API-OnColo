from django.urls import include, path

urlpatterns = [
    path('paciente/', include('paciente.urls')),
    path('administrador/', include('administracao.urls')),
    path('instituicao/', include('instituicao.urls')),
    path('fisioterapeuta/', include('fisioterapeuta.urls')),
    path('consulta/', include('consulta.urls')),

    path('formulario/AFM/', include('formularios.formAFM.urls')),
    path('formulario/AGPG/', include('formularios.formAGPG.urls')),
    path('formulario/AICS/', include('formularios.formAICS.urls')),

    path('formulario/FSFI/', include('formularios.formFSFI.urls')),
    path('formulario/FIQL/', include('formularios.formFIQL.urls')),
    path('formulario/APR/', include('formularios.formAPR.urls')),

    path('formulario/KHQ', include('formularios.formKHQ.urls')),
    path('formulario/QVC/', include('formularios.formQVC.urls')),
    path('formulario/QVCC/', include('formularios.formQVCC.urls')),

    path('formularios/', include('formularios.urls')),
]
