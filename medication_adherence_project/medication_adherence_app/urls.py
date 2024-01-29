# medication_adherence_app/urls.py
from django.urls import path
from .views import (
    RegisterUserView,
    EmailTokenObtainPairView,
    PatientDetailView,
    HealthcareProviderDetailView,
)
from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
    path("register/", RegisterUserView.as_view(), name="register-user"),
    path("token/obtain/", EmailTokenObtainPairView.as_view(), name="token-create"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token-refresh"),
    path("patient/", PatientDetailView.as_view(), name="patient-detail"),
    path(
        "healthcare-provider/",
        HealthcareProviderDetailView.as_view(),
        name="healthcare-provider-detail",
    ),
]
