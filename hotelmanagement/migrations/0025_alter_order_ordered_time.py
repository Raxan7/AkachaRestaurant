# Generated by Django 4.2.4 on 2023-10-21 07:22

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotelmanagement', '0024_alter_order_ordered_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='ordered_time',
            field=models.DateTimeField(default=datetime.datetime(2023, 10, 21, 7, 22, 55, 310301)),
        ),
    ]
