# Generated by Django 4.2.4 on 2023-10-09 13:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('StockManagerApp', '0002_stockpurchases'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stockpurchases',
            name='goods_bought',
            field=models.TextField(),
        ),
    ]
