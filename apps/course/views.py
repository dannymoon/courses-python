from django.shortcuts import render, HttpResponse, redirect
from models import *

# Create your views here.
def index(request):
    response = "working"
    return HttpResponse(response)

def courses(request):
    courses = Course.objects.all()
    data = {
        'courses':courses
    }
    return render(request, 'course/index.html', data )

def destroy(request, course_id):
    return render(request, 'course/destroy.html', {'course':Course.objects.get(id=course_id)})

def add(request):
    Course.objects.create(name=request.POST['input_name'], description=request.POST['input_desc'])
    return redirect('/courses')

def remove(request, course_id):
    Course.objects.get(id=course_id).delete()
    return redirect('/courses')

def no(request):
    return redirect('/courses')
        