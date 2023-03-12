from rest_framework import serializers
from .models import Fisioterapeuta
from projetoinca.validators import *

class FisioterapeutaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fisioterapeuta
        fields = '__all__'

    def to_internal_value(self, data):
        data._mutable = True
        data['nome'] = " ".join(data['nome'].split())

        return super(FisioterapeutaSerializer, self).to_internal_value(data)
    
    def validate(self, data):
        matricula_valida(data['matricula'])
        nome_valido(data['nome'])

        return data
