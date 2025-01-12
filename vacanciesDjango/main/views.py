from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request, 'main/index.html')


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