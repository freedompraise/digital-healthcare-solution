# medication_adherence_app/serializers.py

from rest_framework import serializers
from .models import (
    Patient,
    HealthcareProvider,
    AdherenceReport,
    CommunicationLog,
    CustomUser,
)


class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ["id", "name", "email", "password", "user_type"]
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        user = CustomUser.objects.create_user(
            email=validated_data["email"],
            name=validated_data["name"],
            password=validated_data["password"],
            user_type=validated_data["user_type"],
        )
        return user


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
