from django.shortcuts import render
from django.urls import reverse
from .models import *
from django.http import HttpResponseRedirect


def index(request):
    a = Patient.objects.all()
    config = {
        'patients': a
    }
    return render(request, 'patient/index.html',config)


def add(request):
    return render(request, 'patient/add.html')


def reg(request):
    profile = Patient.objects.create(last_name=request.POST['last_name'],
                                     first_name=request.POST['first_name'],
                                     middle_name=request.POST['middle_name'],
                                     phone=request.POST['phone'],
                                     date_of_receipt=request.POST['date_of_receipt'],
                                     date_of_birth=request.POST['date_of_birth'])
    profile.save()
    return HttpResponseRedirect(reverse('patient:index'))
def update(request, id):
    config={
        'patient':Patient.objects.get(id=id)
    }
    return render(request, 'patient/update.html', config)


def upd(request, id):
    profile = Patient.objects.get(id=id)
    profile.last_name = request.POST['last_name']
    profile.first_name = request.POST['first_name']
    profile.middle_name = request.POST['middle_name']
    profile.phone = request.POST['phone']
    profile.date_of_receipt = request.POST['date_of_receipt']
    profile.date_of_birth = request.POST['date_of_birth']
    profile.save()
    return HttpResponseRedirect(reverse('patient:index'))


def delete(request, id):
    Patient.objects.get(id=id).delete()
    return HttpResponseRedirect(reverse('patient:index'))
