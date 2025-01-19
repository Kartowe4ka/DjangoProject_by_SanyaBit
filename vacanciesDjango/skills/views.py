from django.shortcuts import render
from statistic.models import Statistic

# Create your views here.
def skills(request):
    skills = Statistic.objects.filter(stat_class="Навыки", is_active=True)

    data = {
        "skills": skills
    }
    return render(request, 'skills/skills.html', data)