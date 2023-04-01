from .models import FormKHQ
from .serializers import FormKHQSerializer
from rest_framework import viewsets


class FormKHQViewSet(viewsets.ModelViewSet):
    queryset = FormKHQ.objects.all()
    serializer_class = FormKHQSerializer
