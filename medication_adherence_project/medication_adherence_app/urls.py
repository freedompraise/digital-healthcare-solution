# medication_adherence_app/urls.py
from django.urls import path
from .views import RegisterUserView, EmailTokenObtainPairView
from rest_framework_simplejwt.views import (
    TokenRefreshView,
)

urlpatterns = [
    path("register/", RegisterUserView.as_view(), name="register-user"),
    path("token/obtain", EmailTokenObtainPairView.as_view(), name="token-create"),
    path("token/refresh", TokenRefreshView.as_view(), name="token-refresh"),
    # Add other URLs as needed
]
