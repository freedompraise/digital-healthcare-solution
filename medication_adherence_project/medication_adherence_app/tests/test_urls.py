from django.urls import reverse
from rest_framework.test import APITestCase, APIClient
from rest_framework import status
from .utils import create_patient_user, create_provider_user


class UrlsTestCase(APITestCase):
    def setUp(self):
        self.patient_user, self.patient = create_patient_user()
        self.provider_user, self.provider = create_provider_user()
        self.login_url = reverse("token-create")
        self.refresh_url = reverse("token-refresh")
        self.patient_detail_url = reverse("patient-detail")

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
        self.assertTrue("New User" in response.data.get("name"))

    def test_token_obtain_url(self):
        url = reverse("token-create")
        data = {
            "email": self.patient_user.email,
            "password": "password",
        }
        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue("access" in response.data)
        return response.data.get("access")

    def test_token_refresh_url(self):
        login_data = {
            "email": self.patient_user.email,
            "password": "password",
        }
        login_response = self.client.post(self.login_url, login_data, format="json")
        refresh_token = login_response.data.get("refresh")
        refresh_data = {"refresh": refresh_token}
        refresh_response = self.client.post(
            self.refresh_url, refresh_data, format="json"
        )
        self.assertEqual(refresh_response.status_code, status.HTTP_200_OK)
        self.assertTrue("access" in refresh_response.data)

    def test_patient_detail_url(self):
        access_token = self.test_token_obtain_url()
        client = APIClient(HTTP_AUTHORIZATION="Bearer " + access_token)
        client.force_authenticate(user=self.patient_user)
        response = client.get(self.patient_detail_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


#     def test_healthcare_provider_detail_url(self):
#         url = reverse("healthcare-provider-detail")
#         self.client.force_login(self.provider_user)
#         response = self.client.get(url)
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
