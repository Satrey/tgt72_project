# Generated by Django 4.2 on 2023-04-09 05:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('devices', '0004_alter_devicemodel_slag'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='devicemodel',
            name='slag',
        ),
        migrations.AddField(
            model_name='devicemodel',
            name='slug',
            field=models.SlugField(blank=True, max_length=120, null=True, verbose_name='Слаг'),
        ),
    ]
