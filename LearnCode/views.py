from django.core.paginator import Paginator

from course.models import Course
from django.shortcuts import render


def Main(request):
    courses_list = Course.objects.published()
    paginator = Paginator(courses_list, 6)
    page_num = request.GET.get('page')
    courses = paginator.get_page(page_num)
    return render(request, 'main.html', {'courses': courses})
