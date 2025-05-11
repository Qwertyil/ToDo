from django.urls import reverse_lazy
from django.views.generic import DeleteView
from django.views.generic.edit import CreateView, UpdateView
from django.shortcuts import render, get_object_or_404, redirect

from .models import Task, Theme
from .forms import TaskForm, ThemeForm


def index(request, pk=None):
    tasks = Task.objects.filter(is_completed=False)
    theme = 'All'
    if pk:
        theme = get_object_or_404(Theme, pk=pk)
        tasks = tasks.filter(theme=pk)
    context = {
        'tasks': tasks,
        'themes': Theme.objects.all(),
        'theme': theme
    }
    return render(request, 'tasks/index.html', context=context)


def mark_as_completed(request, pk):
    try:
        task = get_object_or_404(Task, pk=pk)
        task.mark_as_completed()
    except:
        pass # TODO can display a warning message if an error occurs while marking a task as completed
    finally:
        return redirect('tasks:index')


def themes(request):
    return render(request, 'tasks/themes.html', context={'themes': Theme.objects.all()})


class ThemeCreateView(CreateView):
    template_name = 'tasks/themes_new.html'
    form_class = ThemeForm
    success_url = reverse_lazy('tasks:themes')


class ThemeDeleteView(DeleteView):
    model = Theme
    template_name = 'tasks/themes_confirm_delete.html'
    success_url = reverse_lazy('tasks:themes')


class TaskEditView(UpdateView):
    model = Task
    fields = ['title', 'additional', 'theme']
    template_name = 'tasks/tasks_full.html'
    success_url = reverse_lazy('tasks:index')


class TaskCreateView(CreateView):
    template_name = 'tasks/tasks_new.html'
    form_class = TaskForm
    success_url = reverse_lazy('tasks:index')


class TaskDeleteView(DeleteView):
    model = Task
    template_name = 'tasks/tasks_confirm_delete.html'
    success_url = reverse_lazy('tasks:index')
