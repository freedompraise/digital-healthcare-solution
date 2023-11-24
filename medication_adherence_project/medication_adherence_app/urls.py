# medication_adherence_app/urls.py
from django.urls import path
from .views import (
    PatientListCreateView,
    PatientDetailView,
    HealthcareProviderListCreateView,
    HealthcareProviderDetailView,
    AdherenceReportListCreateView,
    AdherenceReportDetailView,
    CommunicationLogListCreateView,
    CommunicationLogDetailView,
)


urlpatterns = [
    path("patients/", PatientListCreateView.as_view()),
    path("patients/<int:pk>/", PatientDetailView.as_view()),
    path("healthcare_providers/", HealthcareProviderListCreateView.as_view()),
    path("healthcare_providers/<int:pk>/", HealthcareProviderDetailView.as_view()),
    path("adherence_reports/", AdherenceReportListCreateView.as_view()),
    path("adherence_reports/<int:pk>/", AdherenceReportDetailView.as_view()),
    path("communication_logs/", CommunicationLogListCreateView.as_view()),
    path("communication_logs/<int:pk>/", CommunicationLogDetailView.as_view()),
]
