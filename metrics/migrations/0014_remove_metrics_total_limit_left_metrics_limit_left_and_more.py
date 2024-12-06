# Generated by Django 5.1.2 on 2024-11-20 09:53

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("metrics", "0013_alter_metrics_options"),
        ("preferences", "0007_alter_userprofile_options"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="metrics",
            name="total_limit_left",
        ),
        migrations.AddField(
            model_name="metrics",
            name="limit_left",
            field=models.SmallIntegerField(default=1),
            preserve_default=False,
        ),
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
