# Generated by Django 3.2.4 on 2021-07-05 16:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('jaguareteapp', '0007_rename_usado_product_digital'),
    ]

    operations = [
        
        migrations.AlterField(
            model_name='customer',
            name='user',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='customer', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='shippingaddress',
            name='address',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
