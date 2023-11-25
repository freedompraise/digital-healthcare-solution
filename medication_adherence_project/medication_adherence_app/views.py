# medication_adherence_app/views.py
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny
from .models import CustomUser, HealthcareProvider, Patient
from .serializers import (
    PatientSerializer,
    HealthcareProviderSerializer,
    TokenObtainPairSerializer,
    CustomUserSerializer,
    AdherenceReportSerializer,
    CommunicationLogSerializer,
)
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
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


class EmailTokenObtainPairView(TokenObtainPairView):
    serializer_class = TokenObtainPairSerializer

    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        if response.status_code == status.HTTP_200_OK:
            # Extract user_type from the validated data
            user_type = response.data.get("user_type")
            response.data["user_type"] = user_type
        return response


class PatientListCreateView(generics.ListAPIView):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer

    def get_queryset(self):
        # Filter patients based on the authenticated user
        return Patient.objects.filter(user=self.request.user)


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
