from django.shortcuts import render, redirect
from course.models import Course
from user.forms import UserForm
from user.models import Account
# Create your views here.


def register(request):
    form = UserForm(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            f = form.save()
            Account.objects.create(user_id=f.id)
            return redirect('profile')
    return render(request, 'registration/register.html', {'form': form})


def profile(request):
    return render(request, 'profile.html')

# def profile_edit(request):
#     return render(request, 'profile.html')


def dashboard(request):
    courses = Course.objects.all()
    return render(request, 'admin/dashboard.html', {'courses': courses})
