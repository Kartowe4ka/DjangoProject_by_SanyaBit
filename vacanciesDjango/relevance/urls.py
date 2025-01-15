from django.urls import path
from . import views

app_name = "relevance"

urlpatterns = [
    path('', views.relevance, name="relevance"),
]