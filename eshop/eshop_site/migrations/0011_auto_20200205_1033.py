# Generated by Django 3.0.2 on 2020-02-05 08:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eshop_site', '0010_auto_20200205_1032'),
    ]

    operations = [
        migrations.AlterField(
            model_name='card',
            name='delivery_method',
            field=models.CharField(db_index=True, default=1, max_length=150),
        ),
    ]