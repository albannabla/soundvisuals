from django.http import HttpResponse
from django.shortcuts import render
from .forms import soundform
from . import timeplot, data, fftplot, wavefile


def index(request):
    return render(request, 'index.html', {'osc1': data.osc1, 'freq1': data.freq1, 'osc2': data.osc2, 'freq2': data.freq2, 'osc3': data.osc3, 'freq3': data.freq3})


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
            f = open("audiosite/data.py", "w+")
            f.write("osc1 = '%s'\rosc2 = '%s'\rosc3 = '%s'\rfreq1 = %d\rfreq2 = %d\rfreq3 = %d\r" % (osc1, osc2, osc3, freq1, freq2, freq3))
            f.close()
            return render(request, 'formsubmit.html')
    else:
        form = soundform()

    return render(request, 'form.html', {'form': form})



