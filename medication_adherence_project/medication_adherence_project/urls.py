from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include("medication_adherence_app.urls")),
    # path("accounts/", include("allauth.urls")),
]
