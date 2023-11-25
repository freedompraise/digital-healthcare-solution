# medication_adherence_app/views.py
from rest_framework import generics
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny
from .models import CustomUser, HealthcareProvider, Patient
from .serializers import (
    PatientSerializer,
    HealthcareProviderSerializer,
    CustomUserSerializer,
    AdherenceReportSerializer,
    CommunicationLogSerializer,
)


class RegisterUserView(generics.CreateAPIView):
    """
    View for registering a user (either patient or healthcare provider).
    """

    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    permission_classes = [AllowAny]

    def perform_create(self, serializer):
        user_type = self.request.data.get("user_type")

        if user_type not in ["PT", "HP"]:
            raise serializers.ValidationError(
                "Invalid user type. Please provide 'PT' or 'HP'."
            )

        validated_data = {
            "email": self.request.data.get("email"),
            "name": self.request.data.get("name"),
            "user_type": user_type,
            "password": self.request.data.get("password"),
        }

        user = serializer.create(validated_data)

        if user_type == "PT":
            Patient.objects.create(user=user)
            message = "Patient registered successfully."
        elif user_type == "HP":
            HealthcareProvider.objects.create(user=user)
            message = "Healthcare provider registered successfully."

        return Response({"message": message}, status=status.HTTP_201_CREATED)


class UserLoginView(ObtainAuthToken):
    """
    View for obtaining an authentication token.
    """

    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        token = Token.objects.get(key=response.data["token"])
        user_type = token.user.user_type if token.user else None
        return Response({"token": token.key, "user_type": user_type})


# class PatientListCreateView(generics.ListAPIView):
#     queryset = Patient.objects.all()
#     serializer_class = PatientSerializer


# class PatientDetailView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Patient.objects.all()
#     serializer_class = PatientSerializer


# class HealthcareProviderListCreateView(generics.ListCreateAPIView):
#     queryset = HealthcareProvider.objects.all()
#     serializer_class = HealthcareProviderSerializer


# class HealthcareProviderDetailView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = HealthcareProvider.objects.all()
#     serializer_class = HealthcareProviderSerializer


# class AdherenceReportListCreateView(generics.ListCreateAPIView):
#     queryset = AdherenceReport.objects.all()
#     serializer_class = AdherenceReportSerializer


# class AdherenceReportDetailView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = AdherenceReport.objects.all()
#     serializer_class = AdherenceReportSerializer


# class CommunicationLogListCreateView(generics.ListCreateAPIView):
#     queryset = CommunicationLog.objects.all()
#     serializer_class = CommunicationLogSerializer


# class CommunicationLogDetailView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = CommunicationLog.objects.all()
#     serializer_class = CommunicationLogSerializer
