from django.shortcuts import render
from statistic.models import Statistic

# Create your views here.
def relevance(request):
    relevance = Statistic.objects.filter(stat_class='Востребованность', is_active=True)

    data = {
        'relevance': relevance
    }

    return render(request, 'relevance/relevance.html', data)