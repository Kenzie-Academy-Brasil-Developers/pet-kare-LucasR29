# Generated by Django 4.1.6 on 2023-02-10 13:22

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("traits", "0003_trait_created_at"),
    ]

    operations = [
        migrations.RenameField(
            model_name="trait",
            old_name="name",
            new_name="trait_name",
        ),
    ]
