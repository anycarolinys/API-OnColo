from rest_framework import serializers
from .models import FormQVC

class FormQVCSerializer(serializers.ModelSerializer):
    class Meta:
        model = FormQVC
        fields = '__all__'