# Generated by Django 4.0.4 on 2023-04-19 07:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cross', '0002_alter_crossroad_address_alter_crossroad_latitude_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='crossroad',
            name='number',
            field=models.IntegerField(blank=True, null=True, verbose_name='Номер перекрёстка'),
        ),
    ]
