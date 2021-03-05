from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from .models import Course
from .forms import CourseForm


# Create your views here.
def CreateCourse(request):
    if request.method == 'POST':
        form = CourseForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('courses')
    return render(request, 'course/create.html')


def CourseList(request):
    courses_list = Course.objects.published()
    paginator = Paginator(courses_list, 9)
    page_number = request.GET.get('page')
    courses = paginator.get_page(page_number)
    return render(request, 'course/courses.html', {'courses': courses})


def CourseUpdate(request, course_id):
    course = Course.objects.get(id=course_id)
    if request.method == 'POST':
        form = CourseForm(request.POST, request.FILES, instance=course)
        if form.is_valid():
            form.save()
    return render(request, 'course/update.html', {'course': course})


def CourseDelete(request, course_id):
    course = Course.objects.get(id=course_id)
    course.delete()
    return redirect('courses')



