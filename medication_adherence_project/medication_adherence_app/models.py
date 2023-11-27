# medication_adherence_app/models.py
from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from .utils import (
    administration_route_choices,
    administration_frequency_choices,
    dosage_form_choices,
    gender_choices,
)


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
    gender = models.CharField(
        max_length=1, choices=gender_choices, blank=True, default="O"
    )
    profile_picture = models.ImageField(upload_to="images", blank=True, null=True)
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
    license_id = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return str(self.user)


class Patient(models.Model):
    user = models.OneToOneField(
        CustomUser, on_delete=models.CASCADE, limit_choices_to={"user_type": "PT"}
    )
    healthcare_provider = models.ForeignKey(
        HealthcareProvider, on_delete=models.CASCADE, blank=True, null=True
    )
    allergies = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return str(self.user)


class Medication(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    start_date = models.DateField()
    end_date = models.DateField()
    prescribed_by = models.CharField(max_length=50, blank=True)
    prescribed_in = models.CharField(max_length=100, blank=True)
    dosage_strength = models.CharField(max_length=15)
    dosage_form = models.CharField(
        max_length=3, choices=dosage_form_choices, default="TAB"
    )
    administration_route = models.CharField(
        max_length=3, choices=administration_route_choices, default="PO"
    )
    administration_frequency = models.CharField(
        max_length=50, choices=administration_frequency_choices, default="QD"
    )

    def __str__(self):
        return self.name


class PatientHealthcareProvider(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    healthcare_provider = models.ForeignKey(
        HealthcareProvider, on_delete=models.CASCADE
    )
    invited = models.BooleanField(default=False)
    accepted = models.BooleanField(default=False)
    invitation_token = models.CharField(max_length=255, null=True, blank=True)
    # Add other fields as needed

    def generate_invitation_token(self):
        # Implement logic to generate a unique token (e.g., using secrets module)
        # Set the generated token to self.invitation_token
        pass
