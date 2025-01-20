from django.shortcuts import render
from statistic.models import Statistic

# Create your views here.
def statistic(request):
    statistic = Statistic.objects.filter(is_active=True)

    data = {
        'stats': statistic
    }

    return render(request, 'statistic/statistic.html', data)