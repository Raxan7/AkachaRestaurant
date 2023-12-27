# Generated by Django 4.2.4 on 2023-12-27 15:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotelmanagement', '0065_alter_customuser_customer_profit_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='customer_profit',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=12),
        ),
    ]