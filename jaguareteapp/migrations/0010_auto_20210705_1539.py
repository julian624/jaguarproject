# Generated by Django 3.2.4 on 2021-07-05 18:39

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('jaguareteapp', '0009_remove_order_customer'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='shippingaddress',
            name='customer',
        ),
        migrations.AlterField(
            model_name='shippingaddress',
            name='address',
            field=models.CharField(default=django.utils.timezone.now, max_length=200),
            preserve_default=False,
        ),
    ]
