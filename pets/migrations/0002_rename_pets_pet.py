# Generated by Django 4.1.6 on 2023-02-07 22:59

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("groups", "0002_rename_groups_group"),
        ("traits", "0001_initial"),
        ("pets", "0001_initial"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="Pets",
            new_name="Pet",
        ),
    ]
