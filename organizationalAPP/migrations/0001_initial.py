# Generated by Django 4.1.7 on 2023-03-26 17:40

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Clothes",
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
                ("name", models.CharField(max_length=64)),
                ("brand", models.CharField(max_length=64)),
                (
                    "size",
                    models.CharField(
                        choices=[
                            ("S", "S"),
                            ("M", "M"),
                            ("L", "L"),
                            ("X", "X"),
                            ("XL", "XL"),
                        ],
                        max_length=3,
                    ),
                ),
                ("photo", models.ImageField(blank=True, null=True, upload_to="photos")),
            ],
        ),
    ]
