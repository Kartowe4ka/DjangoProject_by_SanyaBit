from django.urls import path
from . import views

app_name = "geography"

urlpatterns = [
    path('', views.geography, name="geography"),
]