# Generated by Django 4.2.3 on 2023-08-31 15:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="AppliedUserData",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("Firstname", models.CharField(max_length=100)),
                ("Lastname", models.CharField(max_length=100)),
                ("job_role", models.CharField(max_length=100)),
                ("phonenumber", models.CharField(max_length=100)),
                ("address", models.CharField(max_length=100)),
                ("my_image", models.ImageField(blank=True, null=True, upload_to="")),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
