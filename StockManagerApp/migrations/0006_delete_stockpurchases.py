# Generated by Django 4.2.4 on 2023-10-09 19:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('StockManagerApp', '0005_alter_stockpurchases_recorder'),
    ]

    operations = [
        migrations.DeleteModel(
            name='StockPurchases',
        ),
    ]
