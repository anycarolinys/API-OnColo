from .models import FormAPR
from .serializers import FormAPRSerializer
from rest_framework import viewsets


class FormAPRViewSet(viewsets.ModelViewSet):
    queryset = FormAPR.objects.all()
    serializer_class = FormAPRSerializer
