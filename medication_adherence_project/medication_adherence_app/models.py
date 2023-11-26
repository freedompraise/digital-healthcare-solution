# medication_adherence_app/models.py
from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager


class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        """
        Create and return a regular user with an email and password.
        """
        if not email:
            raise ValueError("The Email field must be set")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        """
        Create and return a superuser with an email and password.
        """
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        return self.create_user(email, password, **extra_fields)


class CustomUser(AbstractUser):
    USER_TYPES = [
        ("HP", "Healthcare Provider"),
        ("PT", "Patient"),
        ("AD", "Administrator"),
    ]

    username = None
    name = models.CharField(max_length=25)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=25, blank=True)
    date_of_birth = models.DateField(blank=True, null=True)
    address = models.CharField(max_length=50, blank=True, null=True)
    profile_picture = models.ImageField(upload_to="images", blank=True)
    user_type = models.CharField(max_length=2, choices=USER_TYPES)
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["name", "user_type"]
    objects = CustomUserManager()

    def __str__(self):
        return self.email


class HealthcareProvider(models.Model):
    user = models.OneToOneField(
        CustomUser, on_delete=models.CASCADE, limit_choices_to={"user_type": "HP"}
    )
    clinic_affiliation = models.CharField(max_length=255, blank=True)
    specialization = models.CharField(max_length=50, blank=True)
    license_id_information = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return str(self.user)


class Patient(models.Model):
    user = models.OneToOneField(
        CustomUser, on_delete=models.CASCADE, limit_choices_to={"user_type": "PT"}
    )
    healthcare_provider = models.ForeignKey(
        HealthcareProvider, on_delete=models.CASCADE, blank=True, null=True
    )

    def __str__(self):
        return str(self.user)


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
