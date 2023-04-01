from rest_framework import serializers
from .models import FormFSFI


class FormFSFISerializer(serializers.ModelSerializer):
    class Meta:
        model = FormFSFI
        fields = '__all__'
