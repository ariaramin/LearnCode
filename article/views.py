from django.shortcuts import render
from .forms import ArticleForms

# Create your views here.


def create(request):
    if request.method == 'POST':
        form = ArticleForms(request.POST, request.FILES)
        if form.is_valid():
            form.save()


def read(request):
    pass


def update(request, article_id):
    pass


def delete(request, article_id):
    pass