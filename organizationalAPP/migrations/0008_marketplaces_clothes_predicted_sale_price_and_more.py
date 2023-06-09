# Generated by Django 4.2 on 2023-04-24 09:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organizationalAPP', '0007_clothtype_clothes_cloth_type'),
    ]

    operations = [
        migrations.CreateModel(
            name='Marketplaces',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
            ],
        ),
        migrations.AddField(
            model_name='clothes',
            name='predicted_sale_price',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='clothes',
            name='purchase_price',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='clothes',
            name='sold_price',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='clothes',
            name='marketplaces',
            field=models.ManyToManyField(null=True, to='organizationalAPP.marketplaces'),
        ),
    ]
