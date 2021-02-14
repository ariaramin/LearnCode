from django.shortcuts import render
from .forms import CategoryForms


# Create your views here.

def create(request):
    if request.method == 'POST':
        form = CategoryForms(request.POST, request.FILES)
        if form.is_valid():
            form.save()

    return render(request, 'category.html')
