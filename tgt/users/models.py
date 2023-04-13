from django.db import models
from django.contrib.auth.models import AbstractUser

import datetime


class Department(models.Model):
    department = models.CharField('Отдел', max_length=50)
    slug = models.CharField('Слаг', max_length=70, blank=True)

    class Meta:
        verbose_name = "Отдел"
        verbose_name_plural = "Отделы"

    def __str__(self):
        return self.department
    

class Position(models.Model):
    name = models.CharField(max_length=50, blank=True, null=True)
    slug = models.SlugField(max_length=60, blank=True, null=True)

    class Meta:
        verbose_name = "Должность"
        verbose_name_plural = "Должности"

    def __str__(self):
        return self.name



class CustomUser(AbstractUser):
    middle_name = models.CharField('Отчество', max_length=50, blank=True, null=True)
    date_of_birth = models.DateField(blank=True, null=True, verbose_name='Дата рождения')
    phone_number_work = models.CharField('Рабочий телефон', max_length=16, blank=True, null=True)
    phone_number_mobile = models.CharField('Мобильный телефон', max_length=12, blank=True, null=True)
    department = models.ForeignKey(Department, blank=True, null=True, on_delete=models.CASCADE, verbose_name='Отдел')
    avatar = models.ImageField(upload_to='avatars/', blank=True, null=True) 
    position = models.ForeignKey('Position', blank=True, null=True, on_delete=models.CASCADE, verbose_name='Должность')
    date_of_imployment = models.DateField(blank=True, null=True, verbose_name='Дата трудоустройства')


    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self) -> str:
        return '%s %s %s' (self.first_name, self.middle_name, self.last_name)

    def work_experience(date_of_imployment):
        date_now = datetime.date.today()
        return date_now - date_of_imployment