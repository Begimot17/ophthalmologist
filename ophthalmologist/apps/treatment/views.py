from django.shortcuts import render
from django.urls import reverse
from .models import *
from django.http import HttpResponseRedirect

def index(request):
    a = Treatment.objects.all()
    config = {
        'treatments': a
    }
    return render(request, 'treatment/index.html',config)



def update(request, id):
    a = Diagnosis.objects.all()
    b = AssignTreat.objects.all()
    config={
        'treatment':Treatment.objects.get(id=id),
        'diagnosiss':a,
        'assign_treats':b
    }
    return render(request, 'treatment/update.html', config)


def upd(request, id):
    treat = Treatment.objects.get(id=id)
    treat.diagnosis = Diagnosis.objects.get(id=request.POST['diagnosis'])
    treat.assign_treat = AssignTreat.objects.get(id=request.POST['assign_treat'])
    treat.appointment_procedures = request.POST['appointment_procedures']
    treat.procedures_perform = request.POST['procedures_perform']
    if treat.print:
        if request.POST['visus_no_cor']:
            treat.print.visus_no_cor = request.POST['visus_no_cor']
        if request.POST['sph']:
            treat.print.sph = request.POST['sph']
        if request.POST['cyt']:
            treat.print.cyt = request.POST['cyt']
        if request.POST['ax']:
            treat.print.ax = request.POST['ax']
        if request.POST['visus_in_cor']:
            treat.print.visus_in_cor = request.POST['visus_in_cor']
        if request.POST['bot']:
            treat.print.bot = request.POST['bot']
        if request.POST['eyelids']:
            treat.print.eyelids = request.POST['eyelids']
        if request.POST['eye_pos']:
            treat.print.eye_pos = request.POST['eye_pos']
        if request.POST['conjunctival']:
            treat.print.conjunctival = request.POST['conjunctival']
        if request.POST['p_camera']:
            treat.print.p_camera = request.POST['p_camera']
        if request.POST['pupil']:
            treat.print.pupil = request.POST['pupil']
        if request.POST['iris']:
            treat.print.iris = request.POST['iris']
        if request.POST['crystalline_glass']:
            treat.print.crystalline_glass = request.POST['crystalline_glass']
        if request.POST['dzn']:
            treat.print.dzn = request.POST['dzn']
        if request.POST['vessels']:
            treat.print.vessels = request.POST['vessels']
        if request.POST['maculah']:
            treat.print.maculah = request.POST['maculah']
        if request.POST['diagnose']:
            treat.print.diagnose = request.POST['diagnose']
        if request.POST['recommend']:
            treat.print.recommend = request.POST['recommend']
        treat.print.save()
    else:
        profile = Print.objects.create()
        if request.POST['visus_no_cor']:
            profile.visus_no_cor = request.POST['visus_no_cor']
        if request.POST['sph']:
            profile.sph = request.POST['sph']
        if request.POST['cyt']:
            profile.cyt = request.POST['cyt']
        if request.POST['ax']:
            profile.ax = request.POST['ax']
        if request.POST['visus_in_cor']:
            profile.visus_in_cor = request.POST['visus_in_cor']
        if request.POST['bot']:
            profile.bot = request.POST['bot']
        if request.POST['eyelids']:
            profile.eyelids = request.POST['eyelids']
        if request.POST['eye_pos']:
            profile.eye_pos = request.POST['eye_pos']
        if request.POST['conjunctival']:
            profile.conjunctival = request.POST['conjunctival']
        if request.POST['p_camera']:
            profile.p_camera = request.POST['p_camera']
        if request.POST['pupil']:
            profile.pupil = request.POST['pupil']
        if request.POST['iris']:
            profile.iris = request.POST['iris']
        if request.POST['crystalline_glass']:
            profile.crystalline_glass = request.POST['crystalline_glass']
        if request.POST['dzn']:
            profile.dzn = request.POST['dzn']
        if request.POST['vessels']:
            profile.vessels = request.POST['vessels']
        if request.POST['maculah']:
            profile.maculah = request.POST['maculah']
        if request.POST['diagnose']:
            profile.diagnose = request.POST['diagnose']
        if request.POST['recommend']:
            profile.recommend = request.POST['recommend']
        profile.save()
        treat.print=profile
    treat.save()
    return HttpResponseRedirect(reverse('treatment:index'))


def delete(request, id):
    Treatment.objects.get(id=id).delete()
    return HttpResponseRedirect(reverse('treatment:index'))
