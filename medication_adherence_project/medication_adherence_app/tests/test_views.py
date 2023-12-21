from rest_framework.test import APITestCase
from rest_framework import status
from .utils import create_patient_user, create_provider_user


class ViewsTestCase(APITestCase):
    def setUp(self):
        self.patient_user, self.patient = create_patient_user()

        self.provider_user, self.provider = create_provider_user()

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
