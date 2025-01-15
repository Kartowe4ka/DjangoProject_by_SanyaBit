from django.urls import path
from . import views

app_name = "main"

urlpatterns = [
    path('', views.index, name="home"),
    #path('statistic', views.statistic, name="statistic"),
    #path('relevance', views.relevance, name="relevance"),
    #path('geography', views.geography, name="geography"),
    #path('skills', views.skills, name="skills"),
    #path('vacancies', views.vacancies, name="vacancies")
]
