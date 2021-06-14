from django.contrib.auth.decorators import permission_required
from django.shortcuts import render, redirect
from .models import Session
from course.models import Course
from .forms import SessionForm


# Create your views here.


@permission_required('Session.add_session')
def CreateSession(request, course_id):
    course = Course.objects.get(id=course_id)
    if request.method == 'POST':
        form = SessionForm(request.POST, request.FILES)
        if form.is_valid():
            f = form.save(commit=False)
            f.course_id = course.id
            f.save()
            return redirect('read.session')
    return render(request, 'session/create.html', {'course': course})


def ReadSession(request, course_id):
    context = {
        'course': Course.objects.get(id=course_id),
        'sessions': Session.objects.filter(course_id=course_id)
    }
    return render(request, 'session/read.html', context)


@permission_required('Session.change_session')
def UpdateSession(request, session_id):
    session = Session.objects.get(id=session_id)
    if request.method == 'POST':
        form = SessionForm(request.POST, request.FILES, instance=session)
        if form.is_valid():
            form.save()
            return redirect('read.session')
    return render(request, 'session/update.html', {'session': session})


@permission_required('Session.delete_session')
def DeleteSession(request, session_id):
    session = Session.objects.get(id=session_id)
    session.delete()
    return redirect('read.session')
