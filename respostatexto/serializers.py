from rest_framework import serializers
from .models import RespostaTexto

class RespostaTextoSerializer(serializers.ModelSerializer):
    class Meta:
        model = RespostaTexto
        fields = ('id', 'texto')