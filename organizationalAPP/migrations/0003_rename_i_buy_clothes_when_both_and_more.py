# Generated by Django 4.1.7 on 2023-03-26 17:56

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("organizationalAPP", "0002_clothes_description_clothes_i_buy_and_more"),
    ]

    operations = [
        migrations.RenameField(
            model_name="clothes",
            old_name="i_buy",
            new_name="when_both",
        ),
        migrations.AlterField(
            model_name="clothes",
            name="description",
            field=models.TextField(blank=True, default=""),
        ),
    ]
