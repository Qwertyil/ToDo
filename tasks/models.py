from django.db import models


class Task(models.Model):
    title = models.CharField(max_length=100, verbose_name='Задача')
    additional = models.TextField(verbose_name='Дополнительная информация', null=True, blank=True)
    creation_time = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    is_completed = models.BooleanField(default=False, verbose_name='Выполнена')
    completion_time = models.DateTimeField(null=True, blank=True, verbose_name='Дата выполнения')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'
        ordering = ['is_completed', '-creation_time']
