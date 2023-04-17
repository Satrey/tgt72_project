from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser


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
    position = models.ForeignKey(Position, blank=True, null=True, on_delete=models.CASCADE, verbose_name='Должность')
    date_of_employment = models.DateField(blank=True, null=True, verbose_name='Дата трудоустройства')

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return self.first_name

    @property
    def experience(self):
        if self.date_of_employment:
            date_now = timezone.now().date()
            year = (date_now - self.date_of_employment).days
            year = int(year) // 365
            month = (date_now - self.date_of_employment).days
            month = (int(month) % 365) // 31
            year_str = ''
            month_str = ''
            if 1 < year < 5:
                year_str = 'года'
            elif year == 1:
                year_str = 'год'
            elif year > 5:
                year_str = 'лет'

            if 1<month<5:
                month_str = 'месяца'
            elif month == 1:
                month_str = 'месяц'
            elif month > 5:
                month_str = 'месяцев'
            return str(year) + ' ' + year_str + ' ' + str(month) + ' ' + month_str
        else:
            return 'Стаж отсутствует'

    @property
    def employer_age(self):
        date_now = timezone.now().date()
        year = (date_now - self.date_of_birth).days
        year = int(year) // 365
        text = ''
        if (year % 10 == 0) or (9 >= year % 10 >= 5):
            text += 'лет'
        elif year % 10 == 1:
            text += 'год'
        else:
            text += 'года'

        return str(year) + '  ' + text


