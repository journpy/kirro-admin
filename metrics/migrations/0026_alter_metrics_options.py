# Generated by Django 5.1.2 on 2024-11-28 23:14

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("metrics", "0025_alter_metrics_id"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="metrics",
            options={
                "managed": True,
                "ordering": ["id"],
                "verbose_name_plural": "Metrics",
            },
        ),
    ]