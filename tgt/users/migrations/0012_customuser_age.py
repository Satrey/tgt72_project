# Generated by Django 4.0.4 on 2023-04-13 10:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0011_rename_date_of_imployment_customuser_date_of_employment'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='age',
            field=models.IntegerField(blank=True, null=True, verbose_name='Возраст'),
        ),
    ]
