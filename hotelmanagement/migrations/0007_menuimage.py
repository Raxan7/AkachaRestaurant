# Generated by Django 4.2.4 on 2023-09-12 05:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hotelmanagement', '0006_alter_customuser_profile'),
    ]

    operations = [
        migrations.CreateModel(
            name='MenuImage',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('image', models.ImageField(upload_to='menus/')),
                ('menu_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hotelmanagement.menucategory')),
                ('menu_item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hotelmanagement.menuitem')),
            ],
        ),
    ]
