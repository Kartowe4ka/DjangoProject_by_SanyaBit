from django.shortcuts import render
from statistic.models import Statistic

# Create your views here.
def geography(request):
    geography = Statistic.objects.filter(stat_class="География", is_active=True)

    data = {
        'geography': geography
    }

    return render(request, 'geography/geography.html', data)