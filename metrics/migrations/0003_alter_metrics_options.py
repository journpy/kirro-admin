# Generated by Django 5.1.2 on 2024-11-19 22:34

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("metrics", "0002_alter_metrics_options"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="metrics",
            options={"managed": True, "verbose_name_plural": "Metrics"},
        ),
    ]