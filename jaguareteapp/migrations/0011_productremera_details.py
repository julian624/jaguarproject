# Generated by Django 3.2.4 on 2021-07-06 18:09

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('jaguareteapp', '0010_auto_20210705_1539'),
    ]

    operations = [
        migrations.AddField(
            model_name='productremera',
            name='details',
            field=models.CharField(default=django.utils.timezone.now, max_length=500),
            preserve_default=False,
        ),
    ]