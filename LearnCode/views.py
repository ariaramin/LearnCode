from django.core.paginator import Paginator

from course.models import Course
from django.shortcuts import render


def Main(request):
    courses = Course.objects.published()
    return render(request, 'main.html', {'courses': courses})
