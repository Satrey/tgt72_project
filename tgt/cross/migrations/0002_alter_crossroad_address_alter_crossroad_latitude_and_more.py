# Generated by Django 4.2 on 2023-04-11 03:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cross', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='crossroad',
            name='address',
            field=models.CharField(max_length=100, verbose_name='Адрес'),
        ),
        migrations.AlterField(
            model_name='crossroad',
            name='latitude',
            field=models.FloatField(verbose_name='Широта'),
        ),
        migrations.AlterField(
            model_name='crossroad',
            name='longitude',
            field=models.FloatField(verbose_name='Долгота'),
        ),
    ]
