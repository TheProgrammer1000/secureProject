from django.shortcuts import render
from django.template import loader

# Create your views here.
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


def firstSite(request):
    template = loader.get_template("myfirst.html")
    return HttpResponse(template.render())
