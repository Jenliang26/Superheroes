from django.shortcuts import render
from django.http import HttpResponse
from .models import Heroes

# Create your views here.
def index(request):
    all_heroes = Heroes.objects.all()
    context = {
        'all_heroes': all_heroes
    }
    return render(request, 'heroes/index.html', context)

def detail(request, hero_id):
    detail_hero = Heroes.objects.get(pk=hero_id)
    context = {
        'detail_hero':detail_hero 
    }
    return render(request, 'heroes/detail.html', context)