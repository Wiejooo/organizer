# Generated by Django 4.1.7 on 2023-06-03 15:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("organizationalAPP", "0014_remove_clothtype_size_alter_clothes_marketplaces"),
    ]

    operations = [
        migrations.AddField(
            model_name="clothtype",
            name="cloth_type",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="organizationalAPP.sizes",
            ),
        ),
    ]
