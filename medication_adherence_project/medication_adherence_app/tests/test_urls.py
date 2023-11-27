from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from django.contrib.auth import get_user_model


class UrlsTestCase(TestCase):
    def setUp(self):
        # Create a patient user
        self.patient_user = get_user_model().objects.create_user(
            email="patient@example.com",
            password="password",
            name="Patient User",
            user_type="PT",
        )

        # Create a healthcare provider user
        self.provider_user = get_user_model().objects.create_user(
            email="provider@example.com",
            password="password",
            name="Provider User",
            user_type="HP",
        )

    def test_register_user_url(self):
        url = reverse("register-user")
        data = {
            "name": "New User",
            "email": "newuser@example.com",
            "password": "newpassword",
            "user_type": "PT",
        }
        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_token_obtain_url(self):
        url = reverse("token-create")
        data = {
            "email": "patient@example.com",
            "password": "password",
        }
        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn("access", response.data)

    def test_token_refresh_url(self):
        url = reverse("token-refresh")
        data = {
            "refresh": "refresh_token",
        }
        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn("access", response.data)

    def test_patient_detail_url(self):
        url = reverse("patient-detail")
        self.client.force_login(self.patient_user)
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_healthcare_provider_detail_url(self):
        url = reverse("healthcare-provider-detail")
        self.client.force_login(self.provider_user)
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_healthcare_provider_patients_url(self):
        url = reverse("healthcare-provider-patients")
        self.client.force_login(self.provider_user)
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_healthcare_providers_list_url(self):
        url = reverse("healthcare-provider-patient-detail")
        self.client.force_login(self.patient_user)
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
