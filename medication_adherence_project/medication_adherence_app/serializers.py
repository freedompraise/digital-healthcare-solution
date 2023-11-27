# medication_adherence_app/serializers.py
from django.contrib.auth import get_user_model
from rest_framework import serializers
from rest_framework_simplejwt.serializers import (
    TokenObtainPairSerializer as JwtTokenObtainPairSerializer,
)

from .models import (
    Patient,
    HealthcareProvider,
    CustomUser,
)


class TokenObtainPairSerializer(JwtTokenObtainPairSerializer):
    username_field = get_user_model().USERNAME_FIELD

    def validate(self, attrs):
        data = super().validate(attrs)
        user_type = self.user.user_type if self.user else None
        data["user_type"] = user_type
        return data


class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = [
            "name",
            "email",
            "password",
            "user_type",
            "profile_picture",
            "gender",
            "date_of_birth",
            "address",
            "phone_number",
        ]
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        user = CustomUser.objects.create_user(
            email=validated_data["email"],
            name=validated_data["name"],
            password=validated_data["password"],
            user_type=validated_data["user_type"],
        )
        user.save()
        return user


class PatientSerializer(serializers.ModelSerializer):
    user = CustomUserSerializer()

    class Meta:
        model = Patient
        fields = ["user", "healthcare_provider", "medications", "alergies"]


class HealthcareProviderSerializer(serializers.ModelSerializer):
    user = CustomUserSerializer()

    class Meta:
        model = HealthcareProvider
        fields = ["user", "clinic_affiliation", "specialization", "license_id"]
