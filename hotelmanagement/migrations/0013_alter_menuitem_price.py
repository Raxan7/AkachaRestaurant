# Generated by Django 4.2.4 on 2023-10-09 04:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotelmanagement', '0012_alter_customuser_user_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menuitem',
            name='price',
            field=models.FloatField(),
        ),
    ]
