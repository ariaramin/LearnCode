from django.urls import path, include
from . import views


urlpatterns = [
    path('register/', views.register, name="register"),
    path('profile/', views.profile, name="profile"),
    # path('user/<int:user_id>', views.UpdateUser, name="edit.user"),
    # path('user/<int:user_id>', views.DeleteUser, name="delete.user"),
    path('user/<int:user_id>', views.SetPermission, name="update.user"),
    path('dashboard/', views.dashboard, name="dashboard"),
]