from django.urls import path, include
from . import views


urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('register/', views.register, name="register"),
    path('profile/', views.profile, name="profile"),
    # path('profile/edit', views.profile_edit, name="profile.edit"),
    path('dashboard/', views.dashboard, name="dashboard"),
]