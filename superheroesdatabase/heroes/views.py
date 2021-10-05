from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Heroes
from django.urls import reverse


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

def create(request):
    if request.method == 'POST':
        super_hero_name = request.POST.get('name')
        alter_ego = request.POST.get('alter_ego')
        primary_power = request.POST.get('primary_power')
        secondary_power = request.POST.get('secondary_power')
        catchphrase = request.POST.get('catchphrase')
        new_hero = Heroes(super_hero_name = super_hero_name, 
        alter_ego = alter_ego, 
        primary_power = primary_power, 
        secondary_power = secondary_power, 
        catchphrase = catchphrase)
        new_hero.save()
        return HttpResponseRedirect(reverse('heroes:index'))
    else:
        return render(request, 'heroes/create.html')

def edit(request, hero_id):
    single_hero = Heroes.objects.get(pk=hero_id)
    context = {
        'single_hero': single_hero
    }
    if request.method == "POST":
        id = single_hero.id
        super_hero_name = request.POST.get('super_hero_name')
        alter_ego = request.POST.get('alter_ego')
        primary_power = request.POST.get('primary_power')
        secondary_power = request.POST.get('secondary_power')
        catchphrase = request.POST.get('catchphrase')
        update_hero = Heroes(id, super_hero_name, alter_ego, primary_power, secondary_power, catchphrase)
        update_hero.save()
        return HttpResponseRedirect(reverse('heroes:index'))
    else:
        return render(request, 'heroes/edit.html', context)

def delete(request, hero_id):
    delete = Heroes.objects.get(pk=hero_id)
    delete.delete()
    return HttpResponseRedirect(reverse('heroes:index'))