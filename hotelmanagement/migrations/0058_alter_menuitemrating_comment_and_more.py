# Generated by Django 4.2.4 on 2023-12-24 07:14

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hotelmanagement', '0057_merge_20231224_0904'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menuitemrating',
            name='comment',
            field=models.TextField(default='No comment', max_length=200),
        ),
        migrations.AlterField(
            model_name='menuitemrating',
            name='menu_item',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='hotelmanagement.menuitem'),
        ),
        migrations.AlterField(
            model_name='menuitemrating',
            name='user',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='order',
            name='ordered_time',
            field=models.DateTimeField(default=datetime.datetime(2023, 12, 24, 7, 14, 38, 328310)),
        ),
        migrations.CreateModel(
            name='Cupon',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('ammount', models.DecimalField(decimal_places=2, max_digits=7)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]