from django.shortcuts import render
from statistic.models import Statistic

# Create your views here.
def skills(request):
    skills = Statistic.objects.get(name='ТОП-20 навыков по годам')

    data = {
        "skills": skills
    }
    return render(request, 'skills/skills.html', data)