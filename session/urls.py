from django.urls import path

from . import views

urlpatterns = [
    path('create/<int:course_id>', views.CreateSession, name='create.session'),
    path('read/<int:course_id>', views.ReadSession, name='read.session'),
    path('update/<int:session_id>', views.UpdateSession, name='update.session'),
    path('delete/<int:session_id>', views.DeleteSession, name='delete.session'),
]