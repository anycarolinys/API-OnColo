from rest_framework import serializers
from .models import FormAPR


class FormAPRSerializer(serializers.ModelSerializer):
    class Meta:
        model = FormAPR
        fields = '__all__'
        read_only_fields = ('apr03',)

    def calculo_imc(self, data):
        return round(data['apr01'] / (data['apr02'] * data['apr02']), 2)
    
    def create(self, validated_data):
        apr03 = self.calculo_imc(validated_data)
        
        return FormAPR.objects.create(apr03=apr03, **validated_data)
