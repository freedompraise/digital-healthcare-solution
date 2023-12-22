# medication_adherence_app/urls.py
from django.urls import path
from .views import (
    RegisterUserView,
    LoginView,
    PatientDetailView,
    HealthcareProviderDetailView,
    HealthcareProviderPatientsView,
    HealthcareProviderPatientsView,
)

urlpatterns = [
    path("register/", RegisterUserView.as_view(), name="register-user"),
    path("login/", LoginView.as_view(), name="login"),
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
