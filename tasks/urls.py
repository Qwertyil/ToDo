from django.urls import path

from . import views


app_name = 'tasks'
urlpatterns = [
    path('', views.index, name='index'),
    path('new_task/', views.TaskCreateView.as_view(), name='new_task'),
    path('<int:pk>/', views.TaskEditView.as_view(), name='edit_task'),
    path('completed/<int:pk>/', views.mark_as_completed, name='complete_task')
]
