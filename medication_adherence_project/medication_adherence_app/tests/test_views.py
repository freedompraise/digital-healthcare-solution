from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth import get_user_model
from .models import HealthcareProvider, Patient


class ViewsTestCase(APITestCase):
    def setUp(self):
        # Create a patient user
        self.patient_user = get_user_model().objects.create_user(
            email="patient@example.com",
            password="password",
            name="Patient User",
            user_type="PT",
        )
        self.patient = Patient.objects.create(user=self.patient_user)

        # Create a healthcare provider user
        self.provider_user = get_user_model().objects.create_user(
            email="provider@example.com",
            password="password",
            name="Provider User",
            user_type="HP",
        )
        self.provider = HealthcareProvider.objects.create(user=self.provider_user)

    def test_register_patient(self):
        url = "/api/register/"
        data = {
            "name": "New Patient",
            "email": "newpatient@example.com",
            "password": "newpassword",
            "user_type": "PT",
        }
        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data["message"], "Patient registered successfully.")

    def test_register_healthcare_provider(self):
        url = "/api/register/"
        data = {
            "name": "New Provider",
            "email": "newprovider@example.com",
            "password": "newpassword",
            "user_type": "HP",
        }
        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(
            response.data["message"], "Healthcare provider registered successfully."
        )

    def test_patient_detail_view(self):
        url = "/api/patient/"
        self.client.force_authenticate(user=self.patient_user)
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_healthcare_provider_detail_view(self):
        url = "/api/healthcare-provider/"
        self.client.force_authenticate(user=self.provider_user)
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_healthcare_provider_patients_view(self):
        url = "/api/healthcare-provider/patients/"
        self.client.force_authenticate(user=self.provider_user)
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_healthcare_providers_list_view(self):
        url = "/api/healthcare-providers/"
        self.client.force_authenticate(user=self.patient_user)
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
