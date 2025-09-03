from django.urls import reverse_lazy
from django.views.generic import DeleteView
from django.views.generic.edit import CreateView, UpdateView
from django.views.decorators.http import require_POST
from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Q, Count

from .models import Task, Theme
from .forms import TaskForm, TaskViewForm, ThemeForm


def make_context(page_name, tasks, request, pk):
    last_visited_page = request.session.get('last_page', None)

    if last_visited_page == page_name:
        if pk:
            theme = get_object_or_404(Theme, pk=pk)
            tasks = tasks.filter(theme=pk)
            request.session['theme'] = theme.name
        else:
            theme = 'All'
            request.session['theme'] = 'All'
    else:
        if 'theme' in request.session and request.session.get('theme') != 'All':
            theme_name = request.session['theme']
            theme = get_object_or_404(Theme, name=theme_name)
            tasks = tasks.filter(theme=theme.pk)
            request.session['theme'] = theme_name
        else:
            theme = 'All'
            request.session['theme'] = 'All'
    context = {
        'tasks_count': Task.objects.filter(is_completed=False).count(),
        'tasks': tasks,
        'themes': Theme.objects.annotate(
            task_count=Count('tasks', filter=Q(tasks__is_completed=False))
        ),
        'theme': theme
    }
    request.session['last_page'] = page_name
    return context


def index(request, pk=None):
    tasks = Task.objects.filter(is_completed=False)
    context = make_context('main', tasks, request, pk)
    return render(request, 'tasks/index.html', context=context)


def show_completed_tasks(request, pk=None):
    tasks = Task.objects.filter(is_completed=True)
    context = make_context('completed', tasks, request, pk)
    return render(request, 'tasks/tasks_completed.html', context=context)


def settings(request):
    request.session['last_page'] = 'settings'
    return render(request, 'tasks/coming_soon.html')


def periodic(request):
    request.session['last_page'] = 'periodic'
    return render(request, 'tasks/coming_soon.html')


@require_POST
def mark_as_completed(request, pk):
    try:
        task = get_object_or_404(Task, pk=pk)
        task.mark_as_completed()
    except:
        pass # TODO can remake to display a warning message if an error occurs while marking a task as completed
    finally:
        request.session['last_page'] = 1
        return redirect('tasks:index')


@require_POST
def delete_completed_task(request, pk):
    try:
        get_object_or_404(Task, pk=pk).delete()
    except:
        pass # TODO can remake to display a warning message if an error occurs while marking a task as completed
    finally:
        request.session['last_page'] = 1
        return redirect('tasks:completed_tasks')


class ThemeCreateView(CreateView):
    template_name = 'tasks/themes_new.html'
    form_class = ThemeForm
    success_url = reverse_lazy('tasks:index')

    def dispatch(self, request, *args, **kwargs):
        response = super().dispatch(request, *args, **kwargs)
        request.session['last_page'] = 1
        return response


class ThemeDeleteView(DeleteView):
    model = Theme
    template_name = 'tasks/themes_confirm_delete.html'
    success_url = reverse_lazy('tasks:index')

    def dispatch(self, request, *args, **kwargs):
        response = super().dispatch(request, *args, **kwargs)
        request.session['last_page'] = 1
        return response


class TaskDetailView(UpdateView):
    model = Task
    form_class = TaskViewForm
    template_name = 'tasks/tasks_completed_info.html'
    success_url = reverse_lazy('tasks:completed_tasks')


class TaskEditView(UpdateView):
    model = Task
    fields = ['title', 'additional', 'theme']
    template_name = 'tasks/tasks_edit.html'
    success_url = reverse_lazy('tasks:index')

    def dispatch(self, request, *args, **kwargs):
        response = super().dispatch(request, *args, **kwargs)
        request.session['last_page'] = 1
        return response


class TaskCreateView(CreateView):
    template_name = 'tasks/tasks_new.html'
    form_class = TaskForm
    success_url = reverse_lazy('tasks:index')

    def get_initial(self):
        initial = super().get_initial()
        theme = self.request.GET.get('theme')
        if theme and theme != 'All':
            theme_object = get_object_or_404(Theme, name=theme)
            initial['theme'] = theme_object
        return initial

    def dispatch(self, request, *args, **kwargs):
        response = super().dispatch(request, *args, **kwargs)
        request.session['last_page'] = 1
        return response


class TaskDeleteView(DeleteView):
    model = Task
    template_name = 'tasks/tasks_confirm_delete.html'
    success_url = reverse_lazy('tasks:index')

    def dispatch(self, request, *args, **kwargs):
        response = super().dispatch(request, *args, **kwargs)
        request.session['last_page'] = 1
        return response
