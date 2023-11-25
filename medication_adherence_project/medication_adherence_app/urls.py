# medication_adherence_app/urls.py
from django.urls import path
from .views import RegisterUserView, UserLoginView

urlpatterns = [
    path("register/", RegisterUserView.as_view(), name="register-user"),
    path("login/", UserLoginView.as_view(), name="login"),
    # Add other URLs as needed
]
