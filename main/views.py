from django.shortcuts import render, render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from main.models import Amaakin
# Create your views here.

def amaakinview(request): 
    trial = Amaakin.objects.all()
    context = {}
    context['trial'] = trial
    return render(request, 'amaakin.html', context)