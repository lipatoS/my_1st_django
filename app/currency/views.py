from django.shortcuts import render
from django.http import HttpResponse


def hello_world(request):
    return HttpResponse("+++++++++")


def index(request):
    return render(request, "index.html")
