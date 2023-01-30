# Generated by Django 4.1.5 on 2023-01-20 09:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="contact",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("email", models.EmailField(max_length=254)),
                ("password", models.CharField(max_length=100)),
                ("address", models.CharField(max_length=500)),
                ("city", models.CharField(max_length=100)),
                ("comments", models.CharField(max_length=1000)),
            ],
        ),
    ]
