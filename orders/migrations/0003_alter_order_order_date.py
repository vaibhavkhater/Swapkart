# Generated by Django 3.2.16 on 2022-11-11 06:04

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_alter_order_order_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='order_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 11, 11, 11, 34, 42, 263245)),
        ),
    ]