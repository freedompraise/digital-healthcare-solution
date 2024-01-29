from pathlib import Path
import os
from dotenv import load_dotenv
import dj_database_url
from datetime import timedelta

load_dotenv()

SECRET_KEY = os.getenv("DJANGO_SECRET_KEY")

DEBUG = os.getenv("DEBUG", "0").lower() in ["true", "t", "1"]

ALLOWED_HOSTS = ["*"]

BASE_DIR = Path(__file__).resolve().parent.parent
print(BASE_DIR)

# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.sites",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "cloudinary_storage",
    "cloudinary",
    "corsheaders",
    "rest_framework",
    "rest_framework_simplejwt",
    "medication_adherence_app",
    "sslserver",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": [
        "rest_framework_simplejwt.authentication.JWTAuthentication",
    ],
    "DEFAULT_PERMISSION_CLASSES": [
        "rest_framework.permissions.IsAuthenticated",
    ],
}

SIMPLE_JWT = {
    "SIGNING_KEY": "cronyGlasses",
    "ALGORITHM": "HS256",
    "AUTH_HEADER_TYPES": ("Bearer",),
    "ACCESS_TOKEN_LIFETIME": timedelta(hours=2),
}

ROOT_URLCONF = "medication_adherence_project.urls"

AUTHENTICATION_BACKENDS = ["medication_adherence_app.auth_backends.EmailBackend"]

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

CORS_ALLOW_ALL_ORIGINS = True

ACCESS_CONTROL_ALLOW_ORIGIN = "*"

WSGI_APPLICATION = "medication_adherence_project.wsgi.application"


# Database
if str(os.environ.get("USE_SQLITE")).lower() == "true":
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.sqlite3",
            "NAME": BASE_DIR / "db.sqlite3",
        }
    }
else:
    DATABASES = {
        "default": dj_database_url.parse(
            os.environ.get("DATABASE_URL"), conn_max_age=600
        ),
    }


AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]

AUTH_USER_MODEL = "medication_adherence_app.CustomUser"


LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True

SITE_ID = 1


DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# # Django Allauth Settings
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_USERNAME_REQUIRED = False
ACCOUNT_AUTHENTICATION_METHOD = "email"
ACCOUNT_UNIQUE_EMAIL = True
ACCOUNT_EMAIL_VERIFICATION = "none"
ACCOUNT_SESSION_REMEMBER = True

# Cloudinary Settings
CLOUDINARY_STORAGE = {
    "CLOUDINARY_CLOUD_NAME": os.getenv("CLOUDINARY_CLOUD_NAME"),
    "CLOUDINARY_API_KEY": os.getenv("CLOUDINARY_API_KEY"),
    "CLOUDINARY_API_SECRET": os.getenv("CLOUDINARY_API_SECRET"),
}

DEFAULT_FILE_STORAGE = "cloudinary_storage.storage.MediaCloudinaryStorage"

MEDIA_URL = "/media/"
STATIC_URL = "/static/"
STATIC_ROOT = BASE_DIR / "static"
