from django.contrib.auth.decorators import permission_required
from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from category.models import Category
from user.models import Account
from .models import Course
from .forms import CourseForm


# Create your views here.
@permission_required('Course.add_course')
def create(request):
    categories = Category.objects.all()
    instructors = Account.objects.filter(is_instructor=True)
    if request.method == 'POST':
        form = CourseForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('read.course')
    return render(request, 'course/create.html', {'categories': categories, 'instructors': instructors})


def read(request):
    courses = Course.objects.all()
    return render(request, 'course/read.html', {'courses': courses})


def show(request):
    courses_list = Course.objects.published()
    paginator = Paginator(courses_list, 12)
    page_number = request.GET.get('page')
    courses = paginator.get_page(page_number)
    return render(request, 'course/courses.html', {'courses': courses})


@permission_required('Course.change_course')
def update(request, course_id):
    categories = Category.objects.all()
    course = Course.objects.get(id=course_id)
    instructors = Account.objects.filter(is_instructor=True)
    if request.method == 'POST':
        form = CourseForm(request.POST, request.FILES, instance=course)
        if form.is_valid():
            form.save()
            return redirect('read.course')
    return render(request, 'course/update.html', {'course': course, 'categories': categories, 'instructors': instructors})


@permission_required('Course.delete_course')
def delete(request, course_id):
    course = Course.objects.get(id=course_id)
    course.delete()
    return redirect('read.course')



