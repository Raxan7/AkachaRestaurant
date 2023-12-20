# Generated by Django 4.2.4 on 2023-12-20 02:16

import datetime
import django.contrib.auth.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotelmanagement', '0054_alter_order_ordered_time'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='customuser',
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.AddField(
            model_name='order',
            name='latitude',
            field=models.DecimalField(decimal_places=15, default=35.810966491699226, max_digits=18),
        ),
        migrations.AlterField(
            model_name='order',
            name='ordered_time',
            field=models.DateTimeField(default=datetime.datetime(2023, 12, 20, 5, 16, 52, 306846)),
        ),
    ]
