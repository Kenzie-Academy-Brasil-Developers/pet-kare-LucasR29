# Generated by Django 4.1.6 on 2023-02-10 14:13

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("pets", "0004_alter_pet_weight"),
    ]

    operations = [
        migrations.AlterField(
            model_name="pet",
            name="weight",
            field=models.DecimalField(decimal_places=2, max_digits=5),
        ),
    ]
