# Generated by Django 4.0.4 on 2023-04-13 09:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0009_position_customuser_date_of_birth_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='position',
            name='slug',
            field=models.SlugField(blank=True, max_length=60, null=True),
        ),
    ]
