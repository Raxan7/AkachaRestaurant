# Generated by Django 4.2.4 on 2023-10-09 15:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hotelmanagement', '0013_alter_menuitem_price'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='menuimage',
            name='menu_category',
        ),
    ]