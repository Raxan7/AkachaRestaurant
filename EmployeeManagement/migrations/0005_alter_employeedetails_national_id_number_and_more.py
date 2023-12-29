# Generated by Django 4.2.4 on 2023-12-29 18:42

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('EmployeeManagement', '0004_remove_employeedetails_firstname_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employeedetails',
            name='National_id_number',
            field=models.CharField(default='1232323', max_length=15),
        ),
        migrations.AlterField(
            model_name='employeedetails',
            name='date_of_birth',
            field=models.DateField(default=datetime.date.today),
        ),
        migrations.AlterField(
            model_name='employeedetails',
            name='social_security_number',
            field=models.CharField(default='12343', max_length=20),
        ),
    ]
