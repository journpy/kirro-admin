# Generated by Django 5.1.2 on 2024-11-15 13:18

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("tracker", "0017_alter_jobtracker_job_preferences"),
    ]

    operations = [
        migrations.AlterField(
            model_name="jobtracker",
            name="job_preferences",
            field=models.URLField(
                default="http://127.0.0.1:8000/supabase-query/", editable=False
            ),
        ),
    ]
