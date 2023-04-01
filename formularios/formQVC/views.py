from .models import FormQVC
from .serializers import FormQVCSerializer
from rest_framework import viewsets


class FormQVCViewSet(viewsets.ModelViewSet):
    queryset = FormQVC.objects.all()
    serializer_class = FormQVCSerializer
