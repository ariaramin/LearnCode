from django.shortcuts import render
from category.forms import CategoryForms

# Create your views here.


def create(request):
    if request.method == 'POST':
        form = CategoryForms(request.POST, request.FILES)
        if form.is_valid():
            form.save()


def read(request):
    pass


def update(request, category_id):
    pass


def delete(request, category_id):
    pass