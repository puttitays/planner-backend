from django.urls import path
from . import views


urlpatterns = [
    path('api/quote/', views.Quote_list_api),
    path('api/dailytask/', views.task_list_api),
    path('api/dailytask/<int:pk>/', views.updated_task),
    path('api/monthlygoals/', views.Monthly_Goal),
]