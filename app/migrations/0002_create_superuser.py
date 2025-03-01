from django.utils import timezone
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("app", "0001_initial"),  # Ensure this matches your latest migration
    ]

    def create_superuser(apps, schema_editor):
        from django.contrib.auth import get_user_model

        User = get_user_model()

        # Only create a superuser if no users exist
        if not User.objects.exists():
            superuser = User.objects.create_superuser(
                username="admin", email="admin@example.com", password="admin"
            )
            superuser.last_login = timezone.now()
            superuser.save()

    operations = [migrations.RunPython(create_superuser)]
