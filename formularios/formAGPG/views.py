from .models import FormAGPG
from .serializers import FormAGPGSerializer
from rest_framework import  viewsets

class FormAGPGViewSet(viewsets.ModelViewSet):
    queryset = FormAGPG.objects.all()
    serializer_class = FormAGPGSerializer