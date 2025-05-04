from django.http import JsonResponse
from django.urls import reverse_lazy
from django.views.decorators.http import require_http_methods
from django.views.generic.edit import CreateView
from django.utils import timezone
from django.shortcuts import render

from .models import Task
from .forms import TaskForm


def index(request):
    return render(request, 'tasks/index.html', context={'tasks': Task.objects.filter(is_completed=False)})


@require_http_methods(['PATCH'])
def mark_task_as_completed(request, pk):
    try:
        task = Task.objects.get(pk=pk)
        task.is_completed = True
        task.completion_time = timezone.now()
        task.save()
        # Явно возвращаем успешный ответ

        return JsonResponse({
            'status': 'success',
            'message': 'Задача успешно обновлена'
        }, status=200)

    except Task.DoesNotExist:
        return JsonResponse({
            'status': 'error',
            'message': 'Задача не найдена'
        }, status=404)

    except Exception as e:
        return JsonResponse({
            'status': 'error',
            'message': str(e)
        }, status=500)


class TaskCreateView(CreateView):
    template_name = 'tasks/new_task.html'
    form_class = TaskForm
    success_url = reverse_lazy('tasks:index')

