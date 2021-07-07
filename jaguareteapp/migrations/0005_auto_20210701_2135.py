# Generated by Django 3.2.4 on 2021-07-02 00:35

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('jaguareteapp', '0004_productremera'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='digital',
            new_name='usado',
        ),
        migrations.RemoveField(
            model_name='order',
            name='date_created',
        ),
        migrations.RemoveField(
            model_name='order',
            name='note',
        ),
        migrations.RemoveField(
            model_name='order',
            name='product',
        ),
        migrations.RemoveField(
            model_name='order',
            name='status',
        ),
        migrations.AddField(
            model_name='order',
            name='complete',
            field=models.BooleanField(default=False, null=True),
        ),
        migrations.AddField(
            model_name='order',
            name='data_ordered',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='order',
            name='transaction_id',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='order',
            name='customer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='jaguareteapp.customer'),
        ),
    ]
