# Generated by Django 3.0.2 on 2020-02-05 15:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('eshop_site', '0019_remove_product_arehgaerg'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='categories',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='eshop_site.Categories'),
        ),
    ]
