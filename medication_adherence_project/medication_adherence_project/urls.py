# medication_adherence_project/urls.py

from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from medication_adherence_app.views import PatientViewSet, HealthcareProviderViewSet

router = routers.DefaultRouter()
router.register(r"patients", PatientViewSet)
router.register(r"healthcare-providers", HealthcareProviderViewSet)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include(router.urls)),
    path("api-auth/", include("rest_framework.urls", namespace="rest_framework")),
]
