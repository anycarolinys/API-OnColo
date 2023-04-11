from rest_framework import serializers
from .models import FormAGPG

class FormAGPGSerializer(serializers.ModelSerializer):
    class Meta:
        model = FormAGPG
        fields = '__all__'
