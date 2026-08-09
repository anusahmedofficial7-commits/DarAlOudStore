import os

from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model


class Command(BaseCommand):
    help = "Create or update the Dar Al Oud admin user"

    def handle(self, *args, **options):
        User = get_user_model()

        username = os.environ.get("ADMIN_USERNAME", "admin")
        password = os.environ.get("ADMIN_PASSWORD")

        if not password:
            self.stdout.write(
                self.style.ERROR(
                    "ADMIN_PASSWORD environment variable is missing."
                )
            )
            return

        email = os.environ.get(
            "ADMIN_EMAIL",
            "admin@daraloudstore.com"
        )

        user, created = User.objects.get_or_create(
            username=username,
            defaults={
                "email": email,
                "is_staff": True,
                "is_superuser": True,
                "is_active": True,
            },
        )

        user.email = email
        user.is_staff = True
        user.is_superuser = True
        user.is_active = True
        user.set_password(password)
        user.save()

        if created:
            self.stdout.write(
                self.style.SUCCESS(
                    f"Admin user '{username}' created successfully."
                )
            )
        else:
            self.stdout.write(
                self.style.SUCCESS(
                    f"Admin user '{username}' password updated successfully."
                )
            )
            