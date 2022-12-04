from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
task = ['foo', 'bar', 'fuz']

def index(request):
    return render(request, 'tasks/index.html', {
        "task":task
    })

def add(request):
    return render(request, 'tasks/add.html')