# Generated by Django 3.2.16 on 2022-11-10 18:04

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='order_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 11, 10, 23, 34, 43, 926404)),
        ),
    ]
