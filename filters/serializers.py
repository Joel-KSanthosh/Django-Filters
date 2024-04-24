from rest_framework import serializers
from .models import GenusModel

class GenusSerializer(serializers.ModelSerializer):
    class Meta:
        model = GenusModel
        fields = '__all__'