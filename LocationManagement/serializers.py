from rest_framework import serializers
from .models import *
class LocationCRUDSerializer(serializers.ModelSerializer):
    class Meta:
        model=Regions
        fields='__all__'