# Generated by Django 5.1.2 on 2024-11-15 20:37

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("preferences", "0001_initial"),
        ("tracker", "0019_remove_jobtracker_job_preferences"),
    ]

    operations = [
        migrations.AlterField(
            model_name="jobtracker",
            name="applicant",
            field=models.ForeignKey(
                help_text="Email (ID) of applicant",
                limit_choices_to={"is_staff": False},
                on_delete=django.db.models.deletion.CASCADE,
                to="preferences.userprofile",
                to_field="email",
            ),
        ),
    ]