# Generated by Django 4.2.4 on 2023-10-28 21:02

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotelmanagement', '0029_menuitem_cost_alter_order_ordered_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menuitem',
            name='average_rating',
            field=models.DecimalField(decimal_places=0, default=0, max_digits=1),
        ),
        migrations.AlterField(
            model_name='order',
            name='ordered_time',
            field=models.DateTimeField(default=datetime.datetime(2023, 10, 29, 0, 2, 8, 178130)),
        ),
    ]
