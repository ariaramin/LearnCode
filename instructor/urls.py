from django.urls import path
from . import views

urlpatterns = [
    path('', views.InstructorList, name='instructores'),
    path('<int:instructor_id>', views.InstructorPanel, name='instructore')
]
