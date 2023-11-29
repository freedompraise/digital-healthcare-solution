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
    Medication,
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


class MedicationSerialier(serializers.ModelSerializer):
    class Meta:
        model = Medication
        fields = "__all__"


class PatientSerializer(serializers.ModelSerializer):
    user = CustomUserSerializer()
    medication = MedicationSerialier()

    class Meta:
        model = Patient
        fields = ["user", "healthcare_provider", "medication"]
        depth = 1

    def update(self, instance, validated_data):
        # Update the nested user serializer data
        user_data = validated_data.pop("user", {})
        user_serializer = self.fields["user"]
        user_instance = instance.user
        user_serializer.update(user_instance, user_data)

        # Update the remaining fields of Patient
        instance.healthcare_provider = validated_data.get(
            "healthcare_provider", instance.healthcare_provider
        )

        instance.save()
        return instance


class HealthcareProviderSerializer(serializers.ModelSerializer):
    user = CustomUserSerializer()

    class Meta:
        model = HealthcareProvider
        fields = ["user", "clinic_affiliation", "specialization", "license_id"]
        depth = 1

    def update(self, instance, validated_data):
        # Update the nested user serializer data
        user_data = validated_data.pop("user", {})
        user_serializer = self.fields["user"]
        user_instance = instance.user
        user_serializer.update(user_instance, user_data)

        # Update the remaining fields of HealthcareProvider
        instance.clinic_affiliation = validated_data.get(
            "clinic_affiliation", instance.clinic_affiliation
        )
        instance.specialization = validated_data.get(
            "specialization", instance.specialization
        )
        instance.license_id = validated_data.get("license_id", instance.license_id)

        instance.save()
        return instance
