from django.core.management.base import BaseCommand
import os
from dotenv import load_dotenv
from django.contrib.auth import get_user_model

load_dotenv()


class Command(BaseCommand):
    help = "Creates a superuser."

    def handle(self, *args, **options):
        os.environ["DJANGO_SETTINGS_MODULE"]

        User = get_user_model()
        if not User.objects.filter(email="").exists():
            User.objects.create_superuser(
                email=os.environ.get("SUPERUSER_EMAIL"),
                password=os.environ.get("SUPERUSER_PASSWORD"),
                name="Admin",
                user_type="admin",
            )
            self.stdout.write(self.style.SUCCESS("Superuser created successfully."))
