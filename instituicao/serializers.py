from rest_framework import serializers
from .models import Instituicao
from projetoinca.validators import *

class InstituicaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Instituicao
        fields = '__all__'
        
    def to_internal_value(self, data):
        data._mutable = True
        data['nome'] = " ".join(data['nome'].split())

        return super(InstituicaoSerializer, self).to_internal_value(data)

    def validate(self, data):

        cnpj_valido(data['cnpj'])
        nome_valido(data['nome'])
        
        return data
