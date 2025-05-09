from django.forms import ModelForm

from .models import Task, Theme


class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ('title', 'additional', 'theme')


class ThemeForm(ModelForm):
    class Meta:
        model = Theme
        fields = ('name', )
