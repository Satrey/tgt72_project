from django.db import models


class Task(models.Model):
    """ Модель представляющая текущие задачи организации """

    task_start_date = models.DateTimeField(auto_now_add=True,
                                           verbose_name='Время поступления')
    task_crossroad_address = models.ForeignKey('cross.CrossRoad', blank=True, null=True, on_delete=models.CASCADE,
                                               verbose_name='Перекрёсток')
    task_bug_description = models.TextField(blank=True, null=True, verbose_name='Описание ошибки')
    task_sender = models.CharField(max_length=50, blank=True, null=True, verbose_name='Передал заявку')
    task_receiver = models.ForeignKey('users.CustomUser', on_delete=models.CASCADE, blank=True, null=True,
                                      verbose_name='Принял заявку')
    task_act_number = models.IntegerField(null=True, blank=True, verbose_name='Номер акта наряда')
    task_work_description = models.TextField(null=True, blank=True, verbose_name='Выполненные работы')
    task_end_date = models.DateTimeField(auto_now=True, blank=True, null=True,
                                         verbose_name='Время завершения')
    task_closed = models.BooleanField(default=False, verbose_name='Закрыта')

    def __str__(self):
        return self.task_bug_description

    class Meta:
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'

