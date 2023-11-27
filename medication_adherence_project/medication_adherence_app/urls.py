# medication_adherence_app/urls.py
from django.urls import path
from .views import (
    RegisterUserView,
    EmailTokenObtainPairView,
    PatientDetailView,
    HealthcareProviderDetailView,
    HealthcareProviderPatientsView,
    HealthcareProviderPatientsView,
)
from rest_framework_simplejwt.views import (
    TokenRefreshView,
)

urlpatterns = [
    path("register/", RegisterUserView.as_view(), name="register-user"),
    path("token/obtain", EmailTokenObtainPairView.as_view(), name="token-create"),
    path("token/refresh", TokenRefreshView.as_view(), name="token-refresh"),
    path("patient/", PatientDetailView.as_view(), name="patient-detail"),
    path(
        "healthcare-provider/",
        HealthcareProviderDetailView.as_view(),
        name="healthcare-provider-detail",
    ),
    path(
        "healthcare-provider/patients/",
        HealthcareProviderPatientsView.as_view(),
        name="healthcare-provider-patients",
    ),
    path(
        "healthcare-providers/",
        HealthcareProviderPatientsView.as_view(),
        name="healthcare-provider-patient-detail",
    ),
]
