from django.shortcuts import render
from .models import Instructor


# Create your views here.


def InstructorList(request):
    context = {
        'Instructors': Instructor.objects.all()
    }
    return render(request, 'instructor/instructor_list.html', context)


def InstructorPanel(request, instructor_id):
    context = {
        'Instructor': Instructor.objects.get(instructor_id)
    }
    return render(request, 'instructor/instructor_list.html', context)
