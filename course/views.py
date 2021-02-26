from django.shortcuts import render, redirect
from instructor.models import Instructor
from .models import Course
from .forms import CourseForm


# Create your views here.
def CreateCourse(request):
    instructor = Instructor.objects.get(is_active=1)
    if request.method == 'POST':
        form = CourseForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
    return render(request, 'course/create.html', {'instructor': instructor})


def CourseList(request):
    courses = Course.objects.all()
    return render(request, 'main.html', {'courses': courses})


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