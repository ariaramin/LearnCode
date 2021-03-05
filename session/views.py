from django.shortcuts import render, redirect
from session.forms import SessionForm
# Create your views here.


def CreateSession(request):
    if request.method == 'POST':
        form = SessionForm(request.GET, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('read.session')
    return render(request, 'session/create.html')

