from django.http import HttpResponse
from django.shortcuts import render
from .forms import soundform
from . import timeplot, fftplot, wavefile
from .models import sound
import matplotlib.pyplot as plt
from scipy import signal
import numpy as np


def index(request):
    osc1 = sound.objects.get(id=1).wavetype
    freq1 = sound.objects.get(id=1).frequency
    osc2 = sound.objects.get(id=2).wavetype
    freq2 = sound.objects.get(id=2).frequency
    osc3 = sound.objects.get(id=3).wavetype
    freq3 = sound.objects.get(id=3).frequency
    return render(request, 'index.html', {'osc1': osc1[2:-2], 'freq1': freq1, 'osc2': osc2[2:-2], 'freq2': freq2, 'osc3': osc3[2:-2], 'freq3': freq3})


def get_data(request):
    if request.method == 'POST':
        form = soundform(request.POST)
        if form.is_valid():
            osc1 = form.cleaned_data['osc1']
            freq1 = form.cleaned_data['freq1']
            osc2 = form.cleaned_data['osc2']
            freq2 = form.cleaned_data['freq2']
            osc3 = form.cleaned_data['osc3']
            freq3 = form.cleaned_data['freq3']
            timeplot.timeplot(freq1,osc1,freq2,osc2,freq3,osc3)
            fftplot.fftplot(freq1,osc1,freq2,osc2,freq3,osc3)
            wavefile.render(freq1,osc1,freq2,osc2,freq3,osc3)
            sound.objects.filter(id=1).update(wavetype=osc1)
            sound.objects.filter(id=2).update(wavetype=osc2)
            sound.objects.filter(id=3).update(wavetype=osc3)
            sound.objects.filter(id=1).update(frequency=freq1)
            sound.objects.filter(id=2).update(frequency=freq2)
            sound.objects.filter(id=3).update(frequency=freq3)            
            return render(request, 'formsubmit.html')
    else:
        form = soundform()

    return render(request, 'form.html', {'form': form})



# this is a test to generate a plot without saving it into a picture.... it crashes though! 
def test(request):

    osc1 = sound.objects.get(id=1).wavetype
    freq1 = sound.objects.get(id=1).frequency
    osc2 = sound.objects.get(id=2).wavetype
    freq2 = sound.objects.get(id=2).frequency
    osc3 = sound.objects.get(id=3).wavetype
    freq3 = sound.objects.get(id=3).frequency
    graph = testplot.test(osc1,osc2,osc3,freq1,freq2,freq3)
    return render(request, 'test.html', {'plot': graph})


