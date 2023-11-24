# medication_adherence_app/serializers.py

from rest_framework import serializers
from .models import Patient, HealthcareProvider, AdherenceReport, CommunicationLog


class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = "__all__"


class HealthcareProviderSerializer(serializers.ModelSerializer):
    class Meta:
        model = HealthcareProvider
        fields = "__all__"


class AdherenceReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = AdherenceReport
        fields = "__all__"


class CommunicationLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = CommunicationLog
        fields = "__all__"
