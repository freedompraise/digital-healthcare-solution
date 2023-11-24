# medication_adherence_app/views.py
from rest_framework import generics
from .models import Patient, HealthcareProvider, AdherenceReport, CommunicationLog
from .serializers import (
    PatientSerializer,
    HealthcareProviderSerializer,
    AdherenceReportSerializer,
    CommunicationLogSerializer,
)


class PatientListCreateView(generics.ListCreateAPIView):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer


class PatientDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer


class HealthcareProviderListCreateView(generics.ListCreateAPIView):
    queryset = HealthcareProvider.objects.all()
    serializer_class = HealthcareProviderSerializer


class HealthcareProviderDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = HealthcareProvider.objects.all()
    serializer_class = HealthcareProviderSerializer


class AdherenceReportListCreateView(generics.ListCreateAPIView):
    queryset = AdherenceReport.objects.all()
    serializer_class = AdherenceReportSerializer


class AdherenceReportDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = AdherenceReport.objects.all()
    serializer_class = AdherenceReportSerializer


class CommunicationLogListCreateView(generics.ListCreateAPIView):
    queryset = CommunicationLog.objects.all()
    serializer_class = CommunicationLogSerializer


class CommunicationLogDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = CommunicationLog.objects.all()
    serializer_class = CommunicationLogSerializer
