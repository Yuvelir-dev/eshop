# Generated by Django 3.0.2 on 2020-02-05 12:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eshop_site', '0015_auto_20200205_1419'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categories',
            name='id_cat',
            field=models.PositiveIntegerField(default=0),
        ),
    ]