# Generated by Django 2.2.13 on 2020-06-22 06:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0006_auto_20200622_0619"),
    ]

    operations = [
        migrations.AddField(
            model_name="customtext",
            name="hytryuryu",
            field=models.BigIntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="customtext",
            name="jytut",
            field=models.BigIntegerField(blank=True, null=True),
        ),
    ]
