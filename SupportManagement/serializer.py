from rest_framework import serializers
from SupportManagement.models import TicketingSystem, SupportExperience

class TicketingSystemSerializer(serializers.ModelSerializer):
    class Meta:
        model = TicketingSystem
        fields = '__all__'

class SupportExperienceSerializer(serializers.ModelSerializer):
    class Meta:
        model = SupportExperience
        fields = '__all__'
