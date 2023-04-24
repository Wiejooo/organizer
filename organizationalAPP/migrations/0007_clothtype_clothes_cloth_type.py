# Generated by Django 4.2 on 2023-04-11 13:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('organizationalAPP', '0006_remove_clothes_when_both_alter_clothes_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='ClothType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=64)),
            ],
        ),
        migrations.AddField(
            model_name='clothes',
            name='cloth_type',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='organizationalAPP.clothtype'),
        ),
    ]