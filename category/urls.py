from django.urls import path

from category import views

urlpatterns = [
    path('create', views.create, name='create_category')
]