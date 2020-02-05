# Generated by Django 3.0.2 on 2020-02-03 12:03

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eshop_site', '0003_card_eshopuser'),
    ]

    operations = [
        migrations.CreateModel(
            name='Add_card',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title_product', models.CharField(db_index=True, max_length=150)),
                ('user_name', models.CharField(db_index=True, max_length=150)),
                ('price_product', models.PositiveIntegerField(blank=True, db_index=True, default=0, validators=[django.core.validators.MinValueValidator(0)])),
            ],
        ),
        migrations.CreateModel(
            name='Delivery_method',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('delivery_method', models.CharField(db_index=True, max_length=150)),
                ('delivery_cost', models.PositiveIntegerField(db_index=True, default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title_product', models.CharField(db_index=True, max_length=150)),
                ('user_name', models.CharField(db_index=True, max_length=150)),
                ('delivery_method', models.CharField(db_index=True, max_length=150)),
            ],
        ),
        migrations.DeleteModel(
            name='Card',
        ),
    ]
