from rest_framework import serializers
from .models import FormFIQL

class FormFIQLSerializer(serializers.ModelSerializer):
    class Meta:
        model = FormFIQL
        fields = '__all__'
