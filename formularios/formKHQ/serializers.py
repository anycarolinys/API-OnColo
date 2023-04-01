from rest_framework import serializers
from .models import FormKHQ

class FormKHQSerializer(serializers.ModelSerializer):
    class Meta:
        model = FormKHQ
        fields = '__all__'