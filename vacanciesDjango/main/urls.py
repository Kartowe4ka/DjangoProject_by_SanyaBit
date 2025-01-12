from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('statistic', views.statistic),
    path('relevance', views.relevance),
    path('geography', views.geography),
    path('skills', views.skills),
    path('vacancies', views.vacancies)
]
