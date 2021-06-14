from django.contrib.auth.models import User, Permission
from django.contrib.contenttypes.models import ContentType
from django.shortcuts import render, redirect

from article.models import Article
from course.models import Course
from session.models import Session
from user.forms import UserForm, AccountForm, UserEditForm
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


# def UpdateUser(request, user_id):
#     user = User.objects.get(id=user_id)
#     account = Account.objects.get(user_id=request.user.id)
#     form1 = UserEditForm(request.POST, instance=user)
#     form2 = AccountForm(request.POST, instance=account)
#     if request.method == 'POST':
#         if form1.is_valid() and form2.is_valid():
#             form1.save()
#             form2.save()
#             return redirect('profile')
#     return render(request, 'profile.html', {'user': account, 'form1': form1, 'form2': form2})

def SetPermission(request, user_id):
    Permissions = Permission.objects.all()
    user = User.objects.get(id=user_id)
    if request.method == 'POST':
        content_type = ContentType.objects.get_for_models(Course, Article, Session)
        permission = Permission.objects.get(codename=request.POST['ChoosePermission'], content_type=content_type)
        user.user_permissions.add(permission)
    return render(request, 'admin/permissions.html', {'permissions': Permissions, 'user': user})


def dashboard(request):
    users = Account.objects.all()
    return render(request, 'admin/dashboard.html', {'users': users})
