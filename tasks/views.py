from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView
from django.shortcuts import render, get_object_or_404, redirect

from .models import Task, Theme
from .forms import TaskForm


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
        pass
    finally:
        return redirect('tasks:index')


def themes(request):
    pass


class TaskEditView(UpdateView):
    model = Task
    fields = ['title', 'additional', 'theme']
    template_name = 'tasks/update.html'
    success_url = reverse_lazy('tasks:index')


class TaskCreateView(CreateView):
    template_name = 'tasks/new.html'
    form_class = TaskForm
    success_url = reverse_lazy('tasks:index')

