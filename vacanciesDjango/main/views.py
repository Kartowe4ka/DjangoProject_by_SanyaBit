from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):
    return HttpResponse("<h1>Test</h1>")


def statistic(request):
    return HttpResponse('<h2>Statistic</h2>')


def relevance(request):
    return HttpResponse('<h2>Relevance</h2>')


def geography(request):
    return HttpResponse('<h2>Geography</h2>')


def skills(request):
    return HttpResponse('<h2>Skills</h2>')


def vacancies(request):
    return HttpResponse('<h2>Vacancies</h2>')