from django.shortcuts import render
from category.models import Category
from course.models import Course
from article.models import Article


def Main(request):
    context = {
        'courses': Course.objects.published(),
        'categories': Category.objects.all(),
        'articles': Article.objects.all()
    }
    return render(request, 'main.html', context)
