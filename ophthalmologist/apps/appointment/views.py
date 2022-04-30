from django.shortcuts import render

def index(request):
    return render(request, 'appointment/index.html')
