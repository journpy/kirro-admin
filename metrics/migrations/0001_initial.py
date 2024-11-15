# Generated by Django 5.1.2 on 2024-11-15 20:23

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Metrics",
            fields=[
                ("id", models.BigAutoField(primary_key=True, serialize=False)),
                ("email", models.TextField(blank=True, null=True)),
                ("jobs_applied", models.SmallIntegerField(blank=True, null=True)),
                (
                    "num_of_interviews_landed",
                    models.SmallIntegerField(blank=True, null=True),
                ),
                ("hours_saved", models.SmallIntegerField(blank=True, null=True)),
                ("total_limits", models.SmallIntegerField(blank=True, null=True)),
            ],
            options={
                "db_table": "metrics",
                "managed": False,
            },
        ),
    ]
