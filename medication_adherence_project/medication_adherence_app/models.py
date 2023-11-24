# medication_adherence_app/models.py
from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=25)
    date_of_birth = models.DateField()
    address = models.CharField(max_length=50)
    profile_picture = models.ImageField(upload_to="images", blank=True)


class HealthcareProvider(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    clinic_affiliation = models.CharField(max_length=255)
    specialization = models.CharField(max_length=50)
    license_id_information = models.CharField(max_length=50)


class Patient(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    healthcare_provider = models.ForeignKey(
        HealthcareProvider, on_delete=models.CASCADE
    )


class Medication(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    dosage = models.CharField(max_length=50)
    frequency = models.CharField(max_length=50)
    start_date = models.DateField()
    end_date = models.DateField()
    # TO DO: Add other fields as needed for medications


class AdherenceReport(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    healthcare_provider = models.ForeignKey(
        HealthcareProvider, on_delete=models.CASCADE
    )
    # TO DO: Add other fields as needed for adherence reports


class CommunicationLog(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    healthcare_provider = models.ForeignKey(
        HealthcareProvider, on_delete=models.CASCADE
    )
    # TO DO: Add other fields as needed for communication logs
