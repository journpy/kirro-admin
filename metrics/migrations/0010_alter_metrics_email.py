# Generated by Django 5.1.2 on 2024-11-20 09:23

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("metrics", "0009_rename_total_limits_metrics_total_limit_left_and_more"),
        ("preferences", "0007_alter_userprofile_options"),
    ]

    operations = [
        migrations.AlterField(
            model_name="metrics",
            name="email",
            field=models.ForeignKey(
                db_column="email",
                on_delete=django.db.models.deletion.CASCADE,
                to="preferences.userprofile",
                to_field="email",
            ),
        ),
    ]
