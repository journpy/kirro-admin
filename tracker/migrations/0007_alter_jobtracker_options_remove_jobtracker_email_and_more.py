# Generated by Django 5.1.2 on 2024-11-05 17:40

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        (
            "tracker",
            "0006_jobtracker_email_alter_jobtracker_application_status_and_more",
        ),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="jobtracker",
            options={
                "ordering": ["-user"],
                "verbose_name_plural": "Job Tracker Information",
            },
        ),
        migrations.RemoveField(
            model_name="jobtracker",
            name="email",
        ),
        migrations.AlterField(
            model_name="jobtracker",
            name="user",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to=settings.AUTH_USER_MODEL,
                to_field="email",
            ),
        ),
    ]
