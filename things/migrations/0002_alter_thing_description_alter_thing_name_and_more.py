# Generated by Django 4.2.5 on 2023-10-01 19:15

from django.db import migrations, models
import things.models


class Migration(migrations.Migration):

    dependencies = [
        ("things", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="thing",
            name="description",
            field=models.CharField(blank=True, max_length=120),
        ),
        migrations.AlterField(
            model_name="thing",
            name="name",
            field=models.CharField(max_length=30, unique=True),
        ),
        migrations.AlterField(
            model_name="thing",
            name="quantity",
            field=models.IntegerField(validators=[things.models.valid_quantity]),
        ),
    ]
