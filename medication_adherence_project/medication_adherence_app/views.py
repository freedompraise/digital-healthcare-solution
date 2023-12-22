# medication_adherence_app/views.py
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from .models import CustomUser, HealthcareProvider, Patient
from .serializers import (
    PatientSerializer,
    CustomUserSerializer,
    HealthcareProviderSerializer,
)
import json
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate, login
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator


class RegisterUserView(generics.CreateAPIView):
    """
    View for registering a user (either patient or healthcare provider).
    """

    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    permission_classes = [AllowAny]

    def perform_create(self, serializer):
        user_type = self.request.data.get("user_type")

        if user_type not in ["PT", "HP", "AD"]:
            raise serializers.ValidationError(
                "Invalid user type. Please provide 'PT', 'HP', or 'AD'."
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


@method_decorator(csrf_exempt, name="dispatch")
class LoginView(APIView):
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        # Get the JSON string from the request.data
        content = request.data.get("_content")

        # Parse the JSON string into a Python dictionary
        data = json.loads(content)

        # Get the email and password from the data dictionary
        email = data.get("email")
        password = data.get("password")
        print(request.data)

        user = authenticate(email=email, password=password)
        if user:
            login(request, user)
            user_type = user.user_type
            refresh = RefreshToken.for_user(user)
            return Response(
                {
                    "refresh": str(refresh),
                    "access": str(refresh.access_token),
                    "user_type": user_type,
                }
            )
        else:
            return Response(
                {"detail": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED
            )


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


class HealthcareProviderPatientsView(generics.ListAPIView):
    serializer_class = PatientSerializer

    def get_queryset(self):
        healthcare_provider = self.request.user.healthcareprovider
        return Patient.objects.filter(healthcare_provider=healthcare_provider)


class HealthcareProvidersList(generics.ListAPIView):
    serializer_class = HealthcareProviderSerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        patient = self.request.user.patient
        return HealthcareProvider.objects.filter(patient=patient)
