from django.urls import path

from . import views

urlpatterns = [
    path('create', views.CreateSession, name='create.session'),
    #path('read', views.ReadSession, name='read.session'),
    #path('create', views.CreateSession, name='create.session'),
    #path('create', views.CreateSession, name='create.session'),
]