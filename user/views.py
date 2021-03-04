from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from course.models import Course


# Create your views here.


def register(request):
    form = UserCreationForm(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            redirect('profile')
    return render(request, 'registration/register.html', {'form': form})


def profile(request):
    return render(request, 'profile.html')


def dashboard(request):
    context = {
        'courses': Course.objects.all()
    }
    return render(request, 'admin/dashboard.html', context)
