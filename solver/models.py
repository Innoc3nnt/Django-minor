from django.db import models

class Task(models.Model):
    task = models.CharField(verbose_name="Формулировка  задачи", default="Какое это число: положительное, отрицательное, ноль?", max_length=255)
    num = models.FloatField(verbose_name='Вещественное число')
    current_date = models.DateTimeField(verbose_name="Дата создания", auto_now=True)
    new_field_that_work = models.FloatField(verbose_name='WORKING!!')


    def __str__(self) -> str:
        return f'{self.id} {self.task}'
    
    class Meta:
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'
        ordering = ('-id',)