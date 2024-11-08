# Generated by Django 4.2.4 on 2023-11-03 10:14

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotelmanagement', '0041_menuitem_item_profit_alter_order_ordered_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menuitemrating',
            name='rating',
            field=models.DecimalField(decimal_places=1, max_digits=2),
        ),
        migrations.AlterField(
            model_name='order',
            name='ordered_time',
            field=models.DateTimeField(default=datetime.datetime(2023, 11, 3, 13, 14, 36, 83128)),
        ),
    ]
