from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.


def index(request):
    return render(request, 'main/index.html')


def about(request):
    return render(request, 'main/about.html')


def explication(request):
    return render(request, 'main/usings_app.html')

def download(request):
    return render(request, 'main/download.html')

def history(request):
    return render(request, 'main/history.html')