from .models import RespostaTexto
from .serializers import RespostaTextoSerializer
from rest_framework import viewsets

class RespostaTextoViewSet(viewsets.ModelViewSet):
    queryset = RespostaTexto.objects.all()
    serializer_class = RespostaTextoSerializer