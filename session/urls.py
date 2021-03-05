from django.urls import path

from . import views

urlpatterns = [
    path('create', views.CreateSession, name='create.session'),
    #path('show', views.ShowSession, name='show.session'),
    #path('create', views.CreateSession, name='create.session'),
    #path('create', views.CreateSession, name='create.session'),
]