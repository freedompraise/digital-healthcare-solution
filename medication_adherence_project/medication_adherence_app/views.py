# medication_adherence_app/views.py
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny
from .models import CustomUser, HealthcareProvider, Patient
from .serializers import (
    PatientSerializer,
    TokenObtainPairSerializer,
    CustomUserSerializer,
    HealthcareProviderSerializer,
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


class PatientDetailView(generics.RetrieveUpdateAPIView):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer

    def get_object(self):
        # Retrieve the patient associated with the logged-in user
        return self.queryset.get(user=self.request.user)

    def retrieve(self, request, *args, **kwargs):
        patient = self.get_object()
        serializer = self.get_serializer(patient)
        return Response(serializer.data)

    def update(self, request, *args, **kwargs):
        patient = self.get_object()
        serializer = self.get_serializer(patient, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)


class HealthcareProviderDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = HealthcareProvider.objects.all()
    serializer_class = HealthcareProviderSerializer

    def get_object(self):
        # Retrieve the healthcare provider associated with the logged-in user
        return self.queryset.get(user=self.request.user)

    def retrieve(self, request, *args, **kwargs):
        healthcare_provider = self.get_object()
        serializer = self.get_serializer(healthcare_provider)
        return Response(serializer.data)

    def update(self, request, *args, **kwargs):
        healthcare_provider = self.get_object()
        serializer = self.get_serializer(
            healthcare_provider, data=request.data, partial=True
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)


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
