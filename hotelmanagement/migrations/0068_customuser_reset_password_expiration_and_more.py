# Generated by Django 4.2.4 on 2023-12-30 11:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotelmanagement', '0067_alter_employee_salary_alter_menuitem_ingredient_cost_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='reset_password_expiration',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='customuser',
            name='reset_password_token',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
