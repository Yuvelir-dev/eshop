# Generated by Django 3.0.2 on 2020-02-05 14:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eshop_site', '0016_auto_20200205_1425'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categories',
            name='id_cat',
            field=models.PositiveIntegerField(blank=True, default=0),
        ),
    ]
