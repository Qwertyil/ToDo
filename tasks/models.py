from django.db import models
from django.urls import reverse
from django.utils import timezone


class Task(models.Model):
    title = models.CharField(max_length=100, verbose_name='Задача')
    additional = models.TextField(verbose_name='Дополнительная информация', null=True, blank=True)
    creation_time = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    is_completed = models.BooleanField(default=False, verbose_name='Выполнена')
    completion_time = models.DateTimeField(null=True, blank=True, verbose_name='Дата выполнения')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('tasks:edit_task', kwargs={'pk': self.pk})

    def mark_as_completed(self):
        self.is_completed = True
        self.completion_time = timezone.now()  # Устанавливаем текущую дату
        self.save()

    class Meta:
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'
        ordering = ['is_completed', '-creation_time']
