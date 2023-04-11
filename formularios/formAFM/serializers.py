from rest_framework import serializers

from ..funcoes import attempt_json_deserialize
from respostatexto.serializers import RespostaTextoSerializer
from respostatexto.models import RespostaTexto
from consulta.serializers import ConsultaSerializer
from .models import FormAFM


class FormAFMSerializer(serializers.ModelSerializer):
    afm06 = RespostaTextoSerializer(read_only=True, many=True)
    afm33 = RespostaTextoSerializer(read_only=True, many=True)
    consulta = ConsultaSerializer(read_only=True)
    
    class Meta:
        model = FormAFM
        fields = '__all__'
    
    def create(self, validated_data):
        request = self.context['request']

        afm06_data = request.data.get('afm06')
        afm06_data = attempt_json_deserialize(afm06_data, expect_type=list)
        afm06_objs = [RespostaTexto.objects.create(**data) for data in afm06_data]
        validated_data['afm06'] = afm06_objs

        afm33_data = request.data.get('afm33')
        afm33_data = attempt_json_deserialize(afm33_data, expect_type=list)
        afm33_objs = [RespostaTexto.objects.create(**data) for data in afm33_data]
        validated_data['afm33'] = afm33_objs

        consulta_pk = request.data.get('consulta')
        validated_data['consulta_id'] = consulta_pk

        instance = super().create(validated_data)

        return instance
    
    def update(self, instance, validated_data):
        request = self.context['request']

        # afm06_data = request.data.get('afm06')
        # validated_data['afm06_id'] = afm06_data

        # afm06_data = request.data.get('afm06')
        # afm06_data = attempt_json_deserialize(afm06_data, expect_type=list)
        # validated_data['afm06'] = afm06_data
        
        afm06_data = request.data.get('afm06')
        afm06_data = attempt_json_deserialize(afm06_data, expect_type=list)
        afm06_objs = [RespostaTexto.objects.create(**data) for data in afm06_data]
        validated_data['afm06'] = afm06_objs

        afm33_data = request.data.get('afm33')
        afm33_data = attempt_json_deserialize(afm33_data, expect_type=list)
        afm33_objs = [RespostaTexto.objects.create(**data) for data in afm33_data]
        validated_data['afm33'] = afm33_objs

        consulta_pk = request.data.get('consulta')
        validated_data['consulta_id'] = consulta_pk

        instance = super().update(instance, validated_data)
        return instance