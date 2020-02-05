# Generated by Django 3.0.2 on 2020-02-03 15:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('eshop_site', '0007_order_count'),
    ]

    operations = [
        migrations.AddField(
            model_name='card',
            name='product',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='rel_product', to='eshop_site.Product'),
            preserve_default=False,
        ),
    ]
