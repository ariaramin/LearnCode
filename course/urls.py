from django.urls import path
from . import views

urlpatterns = [
    path('create', views.create, name='create.course'),
    path('read', views.read, name='read.course'),
    path('', views.show, name='courses'),
    path('update/<int:course_id>', views.update, name='update.course'),
    path('delete/<int:course_id>', views.delete, name='delete.course'),
]
