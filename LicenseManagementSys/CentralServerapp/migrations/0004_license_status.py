# Generated by Django 5.1.2 on 2024-10-09 11:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CentralServerapp', '0003_license_deviceno'),
    ]

    operations = [
        migrations.AddField(
            model_name='license',
            name='status',
            field=models.CharField(choices=[('approved', 'Approved'), ('pending', 'Pending'), ('failed', 'Failed')], default='pending', max_length=20),
        ),
    ]
