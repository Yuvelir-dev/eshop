# Generated by Django 3.0.2 on 2020-02-03 15:04

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eshop_site', '0006_card_count'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='count',
            field=models.PositiveIntegerField(blank=True, db_index=True, default=1, validators=[django.core.validators.MinValueValidator(0)]),
        ),
    ]