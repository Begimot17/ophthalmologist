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
