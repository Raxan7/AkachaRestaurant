# Generated by Django 4.2.4 on 2023-12-29 17:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('EmployeeManagement', '0002_alter_legaldocuments_curriculam_vitae_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='employeedetails',
            name='user',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]