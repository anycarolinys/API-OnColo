from .models import FormFSFI
from .serializers import FormFSFISerializer
from rest_framework import viewsets


class FormFSFIViewSet(viewsets.ModelViewSet):
    queryset = FormFSFI.objects.all()
    serializer_class = FormFSFISerializer
