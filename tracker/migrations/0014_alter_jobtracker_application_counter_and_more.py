# Generated by Django 5.1.2 on 2024-11-12 10:36

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("tracker", "0013_jobtracker_job_preferences"),
    ]

    operations = [
        migrations.AlterField(
            model_name="jobtracker",
            name="application_counter",
            field=models.PositiveIntegerField(blank=True, editable=False, null=True),
        ),
        migrations.AlterField(
            model_name="jobtracker",
            name="job_preferences",
            field=models.JSONField(default=dict),
        ),
    ]
