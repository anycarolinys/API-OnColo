from rest_framework.views import APIView
from rest_framework.response import Response

from formularios.formAPR.models import FormAPR
from formularios.formFIQL.models import FormFIQL
from formularios.formFSFI.models import FormFSFI
from formularios.formKHQ.models import FormKHQ
from formularios.formQVC.models import FormQVC
from formularios.formQVCC.models import FormQVCC
from paciente.models import Paciente

from formularios.formAPR.serializers import FormAPRSerializer
from formularios.formFIQL.serializers import FormFIQLSerializer
from formularios.formFSFI.serializers import FormFSFISerializer
from formularios.formKHQ.serializers import FormKHQSerializer
from formularios.formQVC.serializers import FormQVCSerializer
from formularios.formQVCC.serializers import FormQVCCSerializer

class FormulariosView(APIView):
    def get(self, request):
        queryset1 = FormAPR.objects.all()
        queryset2 = FormFIQL.objects.all()
        queryset3 = FormFSFI.objects.all()
        queryset4 = FormKHQ.objects.all() 
        queryset5 = FormQVC.objects.all() 
        queryset6 = FormQVCC.objects.all() 

        serializer1 = FormAPRSerializer(queryset1, many=True)
        serializer2 = FormFIQLSerializer(queryset2, many=True)
        serializer3 = FormFSFISerializer(queryset3, many=True)
        serializer4 = FormKHQSerializer(queryset4, many=True)
        serializer5 = FormQVCSerializer(queryset5, many=True)
        serializer6 = FormQVCCSerializer(queryset6, many=True)

        data = {
            'FormAPR': serializer1.data,
            'FormFIQL': serializer2.data,
            'FormFSFI': serializer3.data,
            'FormKHQ': serializer4.data,
            'FormQVC': serializer5.data,
            'FormQVCC': serializer6.data,
        }

        return Response(data)

class FormulariosPorPacienteView(APIView):
    def get(self, request, paciente_id):

        paciente = Paciente.objects.get(id=paciente_id)
        consultas = paciente.consulta_set.all()
        formapr = []
        formfiql = []
        formfsfi = []
        formkhq = []
        formqvc = []
        formqvcc = []

        for consulta in consultas:
            formapr = formapr + [formulario for formulario in consulta.formapr_set.all()]
            formfiql = formfiql + [formulario for formulario in consulta.formfiql_set.all()]
            formfsfi = formfsfi + [formulario for formulario in consulta.formfsfi_set.all()]
            formkhq = formkhq + [formulario for formulario in consulta.formkhq_set.all()]
            formqvc = formqvc + [formulario for formulario in consulta.formqvc_set.all()]
            formqvcc = formqvcc + [formulario for formulario in consulta.formqvcc_set.all()]
        
        serializer1 = FormAPRSerializer(formapr, many=True)
        serializer2 = FormFIQLSerializer(formfiql, many=True)
        serializer3 = FormFSFISerializer(formfsfi, many=True)
        serializer4 = FormKHQSerializer(formkhq, many=True)
        serializer5 = FormQVCSerializer(formqvc, many=True)
        serializer6 = FormQVCCSerializer(formqvcc, many=True)

        data = {
            'FormAPR': serializer1.data,
            'FormFIQL': serializer2.data,
            'FormFSFI': serializer3.data,
            'FormKHQ': serializer4.data,
            'FormQVC': serializer5.data,
            'FormQVCC': serializer6.data,
        }

        return Response(data)
