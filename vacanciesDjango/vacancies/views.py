from django.shortcuts import render
from vacancies.api import get_info

# Create your views here.
def vacancies(request):
    func = get_info()
    data = {
        'data': func
    }
    return render(request, 'vacancies/vacancies.html', data)
