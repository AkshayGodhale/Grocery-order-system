# Generated by Django 4.0.3 on 2022-04-19 15:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0017_product_threshold_value'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='Availability',
        ),
    ]