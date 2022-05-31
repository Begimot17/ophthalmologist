from django.shortcuts import render
from django.urls import reverse
from .models import *
from django.http import HttpResponseRedirect


def index(request):
    a = Inspection.objects.all()
    config = {
        'inspections': a
    }
    return render(request, 'appointment/index.html',config)
