from rest_framework import serializers
from .models import FormQVCC

class FormQVCCSerializer(serializers.ModelSerializer):
    class Meta:
        model = FormQVCC
        fields = '__all__'