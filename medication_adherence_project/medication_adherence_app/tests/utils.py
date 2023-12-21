# medication_adherence_app/tests/test_utils.py
from django.contrib.auth import get_user_model
from medication_adherence_app.models import Patient, HealthcareProvider


def create_patient_user(
    email="patient@example.com", password="password", name="Patient User"
):
    user = get_user_model().objects.create_user(
        email=email,
        password=password,
        name=name,
        user_type="PT",
    )
    return user, Patient.objects.create(user=user)


def create_provider_user(
    email="provider@example.com", password="password", name="Provider User"
):
    user = get_user_model().objects.create_user(
        email=email,
        password=password,
        name=name,
        user_type="HP",
    )
    return user, HealthcareProvider.objects.create(user=user)
