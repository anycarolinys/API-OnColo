from rest_framework import serializers

from ..funcoes import attempt_json_deserialize
from respostatexto.serializers import RespostaTextoSerializer
from respostatexto.models import RespostaTexto
from consulta.serializers import ConsultaSerializer
from .models import FormAICS


class FormAICSSerializer(serializers.ModelSerializer):
    aics11 = RespostaTextoSerializer(read_only=True, many=True)
    aics23 = RespostaTextoSerializer(read_only=True, many=True)
    aics35 = RespostaTextoSerializer(read_only=True, many=True)
    consulta = ConsultaSerializer(read_only=True)
    
    class Meta:
        model = FormAICS
        fields = '__all__'
    
    def create(self, validated_data):
        request = self.context['request']

        aics11_data = request.data.get('aics11')
        aics11_data = attempt_json_deserialize(aics11_data, expect_type=list)
        aics11_objs = [RespostaTexto.objects.create(**data) for data in aics11_data]
        validated_data['aics11'] = aics11_objs

        aics23_data = request.data.get('aics23')
        aics23_data = attempt_json_deserialize(aics23_data, expect_type=list)
        aics23_objs = [RespostaTexto.objects.create(**data) for data in aics23_data]
        validated_data['aics23'] = aics23_objs

        aics35_data = request.data.get('aics35')
        aics35_data = attempt_json_deserialize(aics35_data, expect_type=list)
        aics35_objs = [RespostaTexto.objects.create(**data) for data in aics35_data]
        validated_data['aics35'] = aics35_objs

        consulta_pk = request.data.get('consulta')
        validated_data['consulta_id'] = consulta_pk

        instance = super().create(validated_data)

        return instance
    
    def update(self, instance, validated_data):
        request = self.context['request']
        
        aics11_data = request.data.get('aics11')
        aics11_data = attempt_json_deserialize(aics11_data, expect_type=list)
        aics11_objs = [RespostaTexto.objects.create(**data) for data in aics11_data]
        validated_data['aics11'] = aics11_objs
        
        aics23_data = request.data.get('aics23')
        aics23_data = attempt_json_deserialize(aics23_data, expect_type=list)
        aics23_objs = [RespostaTexto.objects.create(**data) for data in aics23_data]
        validated_data['aics23'] = aics23_objs

        aics35_data = request.data.get('aics35')
        aics35_data = attempt_json_deserialize(aics35_data, expect_type=list)
        aics35_objs = [RespostaTexto.objects.create(**data) for data in aics35_data]
        validated_data['aics35'] = aics35_objs

        consulta_pk = request.data.get('consulta')
        validated_data['consulta_id'] = consulta_pk

        instance = super().update(instance, validated_data)
        return instance