# Generated by Django 5.1.2 on 2024-11-20 08:11

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("metrics", "0007_alter_metrics_hours_saved"),
    ]

    operations = [
        migrations.AlterField(
            model_name="metrics",
            name="hours_saved",
            field=models.FloatField(),
        ),
    ]
