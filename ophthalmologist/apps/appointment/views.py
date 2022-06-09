from django.shortcuts import render
from django.urls import reverse
from .models import *
from patient.models import *
from treatment.models import *
from django.http import HttpResponseRedirect
from datetime import datetime


def index(request):
    a = Inspection.objects.all()
    config = {
        'inspections': a
    }
    return render(request, 'appointment/index.html',config)


def add(request):
    a = Survey.objects.all()
    b = Patient.objects.all()
    config = {
        'surveys': a,
        'clients': b
    }
    return render(request, 'appointment/add.html',config)


def reg(request):
    patient_analysis=Patient_analysis.objects.create(patient=Patient.objects.get(id=request.POST['client']))
    treatment= Treatment.objects.create(patient_analysis=patient_analysis)
    reception = Reception.objects.create(treatment=treatment,
                                         survey_type=Survey.objects.get(id=request.POST['survey_type']),
                                     complains=request.POST['complains'])
    profile = Inspection.objects.create(reception=reception)
    split = request.POST['date_of_receipt']

    profile.time_of_receipt = datetime.strptime(split, "%Y-%m-%dT%H:%M")
    profile.save()
    return HttpResponseRedirect(reverse('appointment:index'))
def update(request, id):
    inspection = Inspection.objects.get(id=id)
    a = Survey.objects.all()
    b = Patient.objects.all()
    time=inspection.time_of_receipt.replace(' ','T')
    config = {
        'surveys': a,
        'clients': b,
        'inspection':inspection,
        'time':time
    }
    return render(request, 'appointment/update.html', config)


def upd(request, id):
    profile = Inspection.objects.get(id=id)

    reception=profile.reception
    patient_analysis=reception.treatment.patient_analysis
    patient_analysis.patient=Patient.objects.get(id=request.POST['client'])
    patient_analysis.save()
    reception.complains = request.POST['complains']
    reception.survey_type=Survey.objects.get(id=request.POST['survey_type'])
    reception.save()
    split = request.POST['date_of_receipt']
    profile.time_of_receipt = datetime.strptime(split,"%Y-%m-%dT%H:%M")
    profile.save()
    return HttpResponseRedirect(reverse('appointment:index'))


def delete(request, id):
    Inspection.objects.get(id=id).delete()
    return HttpResponseRedirect(reverse('appointment:index'))
