"""LearnCode URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from . import views, settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.Main, name='home'),
    path('', include('django.contrib.auth.urls')),
    path('accounts/', include('user.urls')),
    path('course/', include('course.urls')),
    path('session/', include('session.urls')),
    path('category/', include('category.urls')),
    path('article/', include('article.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)