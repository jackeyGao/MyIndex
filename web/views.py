from django.shortcuts import render
from django.shortcuts import render_to_response as rtr

from web.models import APP, Skill, Profile

# Create your views here.


def index(request):
    profile = Profile.get_profile()
    skills = Skill.objects.filter(s_type='SL')
    frameworks = Skill.objects.filter(s_type='FM')
    apps = APP.objects.all()
    return rtr('index.html', locals()) 
