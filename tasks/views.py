from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView
from django.shortcuts import render, get_object_or_404, redirect

from .models import Task
from .forms import TaskForm


def index(request):
    context = {
        'tasks': Task.objects.filter(is_completed=False),
        'themes': {}
    }
    return render(request, 'tasks/index.html', context=context)


def mark_as_completed(request, pk):
    try:
        task = get_object_or_404(Task, pk=pk)
        task.mark_as_completed()
        print('succes')
    except:
        pass
    finally:
        return redirect('tasks:index')


class TaskEditView(UpdateView):
    model = Task
    fields = ['title', 'additional']
    template_name = 'tasks/update.html'
    success_url = reverse_lazy('tasks:index')


class TaskCreateView(CreateView):
    template_name = 'tasks/new.html'
    form_class = TaskForm
    success_url = reverse_lazy('tasks:index')

