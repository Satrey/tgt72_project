# Generated by Django 4.2 on 2023-04-11 06:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('devices', '0009_alter_device_address_alter_device_device_type_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='device',
            name='ip_address',
            field=models.GenericIPAddressField(default='192.168.70.1', verbose_name='IP Адрес устройства'),
        ),
    ]
