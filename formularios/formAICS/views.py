from .models import FormAICS
from .serializers import FormAICSSerializer
from rest_framework import  viewsets

class FormAICSViewSet(viewsets.ModelViewSet):
    queryset = FormAICS.objects.all()
    serializer_class = FormAICSSerializer