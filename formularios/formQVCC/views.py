from .models import FormQVCC
from .serializers import FormQVCCSerializer
from rest_framework import viewsets


class FormQVCViewSet(viewsets.ModelViewSet):
    queryset = FormQVCC.objects.all()
    serializer_class = FormQVCCSerializer
