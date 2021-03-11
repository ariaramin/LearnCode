from django.urls import path
from . import views

urlpatterns = [
    path('create', views.create, name='create.article'),
    path('read', views.read, name='read.article'),
    path('update/<int:article_id>', views.update, name='update.article'),
    path('delete/<int:article_id>', views.delete, name='delete.article'),
]