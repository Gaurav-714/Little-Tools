from rest_framework import serializers
from .models import ConvertedFile

class ConvertedFileSerializer(serializers.ModelSerializer):
    class Meta:
        model = ConvertedFile
        fields = '__all__'
