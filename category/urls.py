from django.urls import path
from . import views

urlpatterns = [
    path('create', views.create, name='create.category'),
    path('read', views.read, name='read.category'),
    path('update/<int:category_id>', views.update, name='update.category'),
    path('delete/<int:category_id>', views.delete, name='delete.category'),
]