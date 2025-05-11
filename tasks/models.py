from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.core.exceptions import ValidationError


def validate_reserved_values(value):
    reserved_values = ['All', 'themes', 'actionBtn']
    if value in reserved_values:
        raise ValidationError(f"Name cannot be '{value}'")


class Theme(models.Model):
    name = models.CharField(max_length=30, unique=True, validators=[validate_reserved_values])

    def __str__(self):
        return self.name


class Task(models.Model):
    title = models.CharField(max_length=100, verbose_name='Task')
    additional = models.TextField(verbose_name='Additional information', null=True, blank=True)
    creation_time = models.DateTimeField(auto_now_add=True, verbose_name='Created at')
    is_completed = models.BooleanField(default=False, verbose_name='Completed')
    completion_time = models.DateTimeField(null=True, blank=True, verbose_name='Completion time')
    theme = models.ForeignKey(Theme, null=True, blank=True, on_delete=models.SET_NULL, verbose_name='Theme')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('tasks:edit_task', kwargs={'pk': self.pk})

    def mark_as_completed(self):
        self.is_completed = True
        self.completion_time = timezone.now()
        self.save()

    class Meta:
        verbose_name = 'Task'
        verbose_name_plural = 'Tasks'
        ordering = ['is_completed', '-creation_time']
