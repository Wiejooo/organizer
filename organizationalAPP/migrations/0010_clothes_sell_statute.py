# Generated by Django 4.2 on 2023-05-18 13:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organizationalAPP', '0009_alter_clothes_marketplaces'),
    ]

    operations = [
        migrations.AddField(
            model_name='clothes',
            name='sell_statute',
            field=models.BooleanField(default=False, verbose_name='Sold'),
        ),
    ]