# Generated by Django 4.2.4 on 2023-10-18 07:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hotelmanagement', '0016_menuitem_average_rating_menuitemrating'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='order_date',
        ),
        migrations.RemoveField(
            model_name='order',
            name='restaurant',
        ),
        migrations.RemoveField(
            model_name='table',
            name='restaurant',
        ),
        migrations.AddField(
            model_name='order',
            name='order_processor',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='processor', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='order',
            name='order_receiver',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='order',
            name='ordered_time',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='order',
            name='received_time',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='order',
            name='send',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='order',
            name='start_processing_time',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='is_active',
            field=models.BooleanField(default=False),
        ),
        migrations.RemoveField(
            model_name='order',
            name='menu_items',
        ),
        migrations.CreateModel(
            name='Messages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time_sent', models.DateTimeField(auto_now=True)),
                ('time_opened', models.DateTimeField(blank=True, null=True)),
                ('opened', models.BooleanField(default=False)),
                ('message', models.TextField()),
                ('message_type', models.CharField(choices=[('Authorization', 'Authorization'), ('Request', 'Request'), ('Denial', 'Denial'), ('Information', 'Information'), ('Unknown', 'Unknown')], default=('Information', 'Information'), max_length=255)),
                ('order', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='hotelmanagement.order')),
                ('receiver_category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='hotelmanagement.user_type')),
                ('sender', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='message_sender', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='order',
            name='menu_items',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='hotelmanagement.menuitem'),
        ),
    ]
