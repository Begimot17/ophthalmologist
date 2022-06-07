from django.shortcuts import render
from django.urls import reverse
from .models import *
from django.http import HttpResponseRedirect


def index(request):
    a = Place.objects.all()
    config = {
        'materials': a
    }
    return render(request, 'materials/index.html',config)

def add(request):
    a = Drug.objects.all()
    config = {
        'drugs': a
    }
    return render(request, 'materials/add.html',config)


def reg(request):
    drug = Drug_Order.objects.create(drug=Drug.objects.get(id=request.POST['drug']),
                                     quantity=request.POST['quantity'])
    profile = Place.objects.create(name=request.POST['name'],
                                     total=request.POST['total'],
                                     remainder=request.POST['remainder'],
                                     open=request.POST['open'],
                                     date_of_delivery=request.POST['date_of_delivery'],
                                     drugs=drug)
    drug.save()
    profile.save()
    return HttpResponseRedirect(reverse('materials:index'))
def update(request, id):
    a = Drug.objects.all()
    config={
        'drugs': a,
        'material':Place.objects.get(id=id)
    }
    return render(request, 'materials/update.html', config)


def upd(request, id):
    profile = Place.objects.get(id=id)
    drug = Drug_Order.objects.create(drug=Drug.objects.get(id=request.POST['drug']),
                                     quantity=request.POST['quantity'])
    profile.name = request.POST['name']
    profile.total = request.POST['total']
    profile.remainder = request.POST['remainder']
    profile.open = request.POST['open']
    profile.date_of_delivery = request.POST['date_of_delivery']
    profile.drugs = drug
    profile.save()
    return HttpResponseRedirect(reverse('materials:index'))


def delete(request, id):
    Place.objects.get(id=id).delete()
    return HttpResponseRedirect(reverse('materials:index'))
