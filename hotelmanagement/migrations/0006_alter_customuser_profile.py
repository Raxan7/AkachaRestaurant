# Generated by Django 4.2.4 on 2023-09-11 05:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotelmanagement', '0005_merge_20230909_1430'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='profile',
            field=models.ImageField(default='profiles/default_profile.jpg', upload_to='profiles/'),
        ),
    ]
