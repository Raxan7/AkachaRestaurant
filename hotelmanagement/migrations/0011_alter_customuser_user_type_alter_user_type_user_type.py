# Generated by Django 4.2.4 on 2023-09-19 11:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotelmanagement', '0010_alter_customuser_user_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='user_type',
            field=models.CharField(default='customer', max_length=50),
        ),
        migrations.AlterField(
            model_name='user_type',
            name='user_type',
            field=models.CharField(max_length=50),
        ),
    ]
