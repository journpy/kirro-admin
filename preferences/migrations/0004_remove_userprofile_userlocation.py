# Generated by Django 5.1.2 on 2024-11-19 02:05

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("preferences", "0003_alter_userprofile_email_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="userprofile",
            name="userlocation",
        ),
    ]