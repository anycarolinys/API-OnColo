from .models import FormFIQL
from .serializers import FormFIQLSerializer
from rest_framework import viewsets


class FormFIQLViewSet(viewsets.ModelViewSet):
    queryset = FormFIQL.objects.all()
    serializer_class = FormFIQLSerializer
