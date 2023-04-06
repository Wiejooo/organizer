# Generated by Django 4.1.7 on 2023-04-05 19:02

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("organizationalAPP", "0004_clothes_slug"),
    ]

    operations = [
        migrations.AlterField(
            model_name="clothes",
            name="size",
            field=models.CharField(
                blank=True,
                choices=[("S", "S"), ("M", "M"), ("L", "L"), ("X", "X"), ("XL", "XL")],
                max_length=3,
                null=True,
            ),
        ),
    ]