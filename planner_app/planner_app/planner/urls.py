from django.urls import path

from . import views

urlpatterns = [
    path('', views.dashboard_view, name='dashboard'),
    path('create-class', views.create_class_view, name='create-class'),
    path('delete-class/<int:id>', views.delete_class_view, name='delete-class'),
    path('class/<int:id>', views.class_view, name='class'),
    path('create-assignment/<int:id>', views.create_assignment, name='create-assignment'),
    path('delete-assignment/<int:id>', views.delete_assignment, name='delete-assignment'),
    path('create-reminder/<int:id>', views.create_reminder, name='create-reminder'),
    path('delete-reminder/<int:id>', views.delete_reminder, name='delete-reminder')
]