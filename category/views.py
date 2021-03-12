from django.shortcuts import render, redirect
from category.forms import CategoryForms
from course.models import Course
from .models import Category
# Create your views here.


def create(request):
    if request.method == 'POST':
        form = CategoryForms(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('read.category')
    return render(request, 'category/create.html')


def read(request):
    categories = Category.objects.all()
    return render(request, 'category/read.html', {'categories': categories})


def update(request, category_id):
    category = Category.objects.get(id=category_id)
    if request.method == 'POST':
        form = CategoryForms(request.POST, request.FILES, instance=category)
        if form.is_valid():
            form.save()
            return redirect('read.category')
    return render(request, 'category/update.html', {'category': category})


def delete(request, category_id):
    category = Category.objects.get(id=category_id)
    category.delete()
    return redirect('read.category')


def show(request, category_id):
    courses = Course.objects.filter(category__course=category_id)
    return render(request, 'category/show.html', {'courses': courses})