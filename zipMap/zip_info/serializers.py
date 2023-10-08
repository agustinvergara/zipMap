from rest_framework import serializers
from .models import *

class postaCodeFormSerializer(serializers.Serializer):
    postal_code = serializers.CharField(max_length=100)

class zipCodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ZipCode
        fields = ['postal_code', 'country_code', 'latitude', 'longitude', 'city', 'province']
        