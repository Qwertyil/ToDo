from django.urls import path

from . import views


app_name = 'tasks'
urlpatterns = [
    path('', views.index, name='index'), # main page
    path('new/', views.TaskCreateView.as_view(), name='new_task'), # new task creation
    path('<int:pk>/', views.TaskEditView.as_view(), name='edit_task'), # task edition
    path('complete/<int:pk>/', views.mark_as_completed, name='complete_task'), # marks task as completed (not a page)
    path('completed/', views.show_completed_tasks, name='completed_tasks'), # shows completed tasks
    path('completed/theme_<int:pk>', views.show_completed_tasks, name='completed_tasks_with_concrete_theme'), # shows completed tasks with concrete theme
    path('completed/<int:pk>/', views.TaskDetailView.as_view(), name='completed_task_info'), # shows completed task info
    path('completed/delete/<int:pk>/', views.delete_completed_task, name='delete_completed_task'), # deletes completed task (not a page)
    path('delete/<int:pk>/', views.TaskDeleteView.as_view(), name='delete_task'), # task deletion
    path('theme_<int:pk>/', views.index, name='tasks_with_concrete_theme'), # shows tasks with concrete theme
    path('themes/new/', views.ThemeCreateView.as_view(), name='new_theme'), # new theme
    path('themes/delete/<int:pk>/', views.ThemeDeleteView.as_view(), name='delete_theme'), # theme deletion
    path('settings/', views.settings, name='settings'), # coming soon
    path('periodic/', views.periodic, name='periodic'), # coming soon
]
