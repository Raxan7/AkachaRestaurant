# Generated by Django 4.2.4 on 2023-09-19 11:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotelmanagement', '0008_user_type_alter_customuser_user_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_type',
            name='user_type',
            field=models.CharField(default='Super', max_length=50),
        ),
    ]
