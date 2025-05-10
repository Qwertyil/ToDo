from django.urls import path

from . import views


app_name = 'tasks'
urlpatterns = [
    path('', views.index, name='index'),
    path('new/', views.TaskCreateView.as_view(), name='new_task'),
    path('<int:pk>/', views.TaskEditView.as_view(), name='edit_task'),
    path('complete/<int:pk>/', views.mark_as_completed, name='complete_task'),
    path('delete/<int:pk>/', views.TaskDeleteView.as_view(), name='delete_task'),
    path('theme_<int:pk>', views.index, name='tasks_with_concrete_theme'),
    path('themes/', views.themes, name='themes'),
    path('themes/new/', views.ThemeCreateView.as_view(), name='new_theme'),
    path('themes/delete/<int:pk>', views.ThemeDeleteView.as_view(), name='delete_theme'),
]
