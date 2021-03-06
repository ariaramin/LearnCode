from django.urls import path
from . import views

urlpatterns = [
    path('create', views.CreateCourse, name='create.course'),
    path('read', views.ReadCourse, name='read.course'),
    path('', views.CourseList, name='courses'),
    path('update/<int:course_id>', views.CourseUpdate, name='update.course'),
    path('delete/<int:course_id>', views.CourseDelete, name='delete.course'),
]
