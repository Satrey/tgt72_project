# Generated by Django 4.2 on 2023-04-08 14:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CrossRoad',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=100)),
                ('latitude', models.FloatField()),
                ('longitude', models.FloatField()),
            ],
            options={
                'verbose_name': 'Перекрёсток',
                'verbose_name_plural': 'Перекрёстки',
            },
        ),
    ]
