##this routine will generate and play sound made by 3 different oscillators plus it will generate plot
## each oscillators can be square or sawtooth or sine (default)
## requires numpy, sounddevice, soundfile and scipy modules




from __future__ import division
import numpy as np
import sounddevice as sd
import soundfile as sf
from scipy import signal
from scipy.fftpack import fft
import matplotlib.pyplot as plt

volume = 0.5  # range [0.0, 1.0]
fs = 44100  # sampling rate, Hz
duration = 2.0  # in seconds
f_1 = 440.0  # frequency, Hz
f_2 = 400.0  # frequency, Hz
f_3 = 470.0  # frequency, Hz
type1 = "saw"
type2 = "sine"
type3 = "sine"
t = np.arange(int(duration * fs)) / fs


if type1 == "saw":
	osc1 = signal.square(2 * np.pi * f_1 * t)
elif type1 == "square":
	osc1 = signal.sawtooth(2 * np.pi * f_1 * t)
else: 
	osc1 = np.sin(2 * np.pi * f_1 * t)

if type2 == "saw":
	osc2 = signal.square(2 * np.pi * f_2 * t)
elif type2 == "square":
	osc2 = signal.sawtooth(2 * np.pi * f_2 * t)
else: 
	osc2 = np.sin(2 * np.pi * f_2 * t)

if type3 == "saw":
	osc3 = signal.square(2 * np.pi * f_3 * t)
elif type3 == "square":
	osc3 = signal.sawtooth(2 * np.pi * f_3 * t)
else: 
	osc3 = np.sin(2 * np.pi * f_3 * t)

samples = volume * (osc1 + osc2 + osc3)
#print(samples)

sd.play(samples, fs)
sd.wait()
fft_out = fft(samples)
plt.plot(samples, np.abs(fft_out))
plt.show()


