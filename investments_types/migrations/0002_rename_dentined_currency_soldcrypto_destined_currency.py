# Generated by Django 4.2 on 2024-07-15 18:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("investments_types", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="soldcrypto",
            old_name="dentined_currency",
            new_name="destined_currency",
        ),
    ]
