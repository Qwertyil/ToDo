from django.forms import ModelForm, DateTimeField

from .models import Task, Theme


class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'additional', 'theme']


class TaskViewForm(ModelForm):
    creation_time = DateTimeField(disabled=True, required=False)
    completion_time = DateTimeField(disabled=True, required=False)

    class Meta:
        model = Task
        fields = ('title', 'additional', 'theme')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.instance and self.instance.pk:
            self.initial['creation_time'] = self.instance.creation_time
            self.initial['completion_time'] = self.instance.completion_time
            for field in self.fields:
                self.fields[field].disabled = True


class ThemeForm(ModelForm):
    class Meta:
        model = Theme
        fields = ('name', )
