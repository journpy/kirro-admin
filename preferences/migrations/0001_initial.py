# Generated by Django 5.1.2 on 2024-11-15 13:45

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="UserProfile",
            fields=[
                ("user_id", models.UUIDField(primary_key=True, serialize=False)),
                ("created_at", models.DateTimeField()),
                ("updated_at", models.DateTimeField(blank=True, null=True)),
                ("email", models.CharField(blank=True, null=True, unique=True)),
                ("first_name", models.TextField(blank=True, null=True)),
                ("last_name", models.TextField(blank=True, null=True)),
                ("phone_number", models.TextField(blank=True, null=True, unique=True)),
                ("profile_picture_url", models.TextField(blank=True, null=True)),
                ("resume_url", models.TextField(blank=True, null=True)),
                ("job_preferences", models.TextField(blank=True, null=True)),
                (
                    "userlocation",
                    models.TextField(blank=True, db_column="userLocation", null=True),
                ),
            ],
            options={
                "db_table": "user_profile",
                "managed": False,
            },
        ),
    ]