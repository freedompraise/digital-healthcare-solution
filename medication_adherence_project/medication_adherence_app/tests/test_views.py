from django.contrib.auth import get_user_model
from rest_framework.test import APITestCase
from rest_framework import status
from .utils import create_patient_user, create_provider_user


class ViewsTestCase(APITestCase):
    def setUp(self):
        self.patient_user, _ = create_patient_user()
        self.patient_data = {
            "email": "patient@example.com",
            "password": "password",
        }
        self.provider_user, _ = create_provider_user()
        self.provider_data = {
            "email": "provider@example.com",
            "password": "password",
        }

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

    # def test_login_patient(self):
    #     url = "/api/login/"
    #     response = self.client.post(url, data=self.patient_data, format="json")

    #     self.assertEqual(response.status_code, status.HTTP_200_OK)

    #     data = response.json()

    #     self.assertIn("access", data)
    #     self.assertIn("refresh", data)
    #     self.assertIn("user_type", data)

    #     self.assertEqual(data["user_type"], "PT")

    # def test_login_healthcare_provider(self):
    #     url = "/api/login/"
    #     response = self.client.post(url, self.provider_data, format="json")

    #     # Debug information
    #     print(response.content.decode("utf-8"))

    #     self.assertEqual(response.status_code, status.HTTP_200_OK)
    #     self.assertIn("access", response.data)
    #     self.assertIn("refresh", response.data)
    #     self.assertIn("user_type", response.data)
    #     self.assertEqual(response.data["user_type"], "HP")

    # def test_patient_detail_view(self):
    #     url = "/api/patient/"
    #     self.client.force_authenticate(user=self.patient_user)
    #     response = self.client.get(url)
    #     self.assertEqual(response.status_code, status.HTTP_200_OK)

    # def test_healthcare_provider_detail_view(self):
    #     url = "/api/healthcare-provider/"
    #     self.client.force_authenticate(user=self.provider_user)
    #     response = self.client.get(url)
    #     self.assertEqual(response.status_code, status.HTTP_200_OK)

    # def test_healthcare_provider_patients_view(self):
    #     url = "/api/healthcare-provider/patients/"
    #     self.client.force_authenticate(user=self.provider_user)
    #     response = self.client.get(url)
    #     self.assertEqual(response.status_code, status.HTTP_200_OK)

    # def test_healthcare_providers_list_view(self):
    #     url = "/api/healthcare-providers/"
    #     self.client.force_authenticate(user=self.patient_user)
    #     response = self.client.get(url)
    #     self.assertEqual(response.status_code, status.HTTP_200_OK)
