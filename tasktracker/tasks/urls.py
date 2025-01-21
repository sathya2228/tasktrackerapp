from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('signup/', views.signup_view, name='signup'),
    
    path('create/', views.create_task, name='create_task'), 
    path('tasks/', views.task_list, name='task_list'), 
    
]
