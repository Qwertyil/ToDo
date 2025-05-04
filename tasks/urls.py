from django.urls import path

from . import views


app_name = 'tasks'
urlpatterns = [
    path('', views.index, name='index'),
    path('new_task/', views.TaskCreateView.as_view(), name='new_task'),
    path('<int:pk>/', views.mark_task_as_completed, name='mark_task_as_completed')
]
