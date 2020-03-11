
from __future__ import division
import numpy as np
from scipy import signal
from scipy.fftpack import fft
import matplotlib.pyplot as plt

volume = 0.5  # range [0.0, 1.0]
fs = 44100  # sampling rate, Hz
duration = 2.0  # in seconds
N = duration * fs 

# f_1 = 440.0  # frequency, Hz
# f_2 = 400.0  # frequency, Hz
# f_3 = 470.0  # frequency, Hz
# type1 = "saw"
# type2 = "sine"
# type3 = "sine"

def fftplot(freq1,osc1,freq2,osc2,freq3,osc3):
	t = np.arange(int(N)) / fs
	period = 1/freq1
	sine_length = np.arange(int(period*fs)) / fs

	if osc1 == ["Sawtooth"]:
		out1 = signal.sawtooth(2 * np.pi * freq1 * t)
	elif osc1 == ["Square"]:
		out1 = signal.square(2 * np.pi * freq1 * t)
	else: 
		out1 = np.sin(2 * np.pi * freq1 * t)

	if osc2 == ["Sawtooth"]:
		out2 = signal.sawtooth(2 * np.pi * freq2 * t)
	elif osc2 == ["Square"]:
		out2 = signal.square(2 * np.pi * freq2 * t)
	else: 
		out2 = np.sin(2 * np.pi * freq2 * t)

	if osc3 == ["Sawtooth"]:
		out3 = signal.sawtooth(2 * np.pi * freq3 * t)
	elif osc3 == ["Square"]:
		out3 = signal.square(2 * np.pi * freq3 * t)
	else: 
		out3 = np.sin(2 * np.pi * freq3 * t)

	samples = volume * (out1 + out2 + out3)
	fft_out = fft(samples)
	xf = np.arange(int(fs))
	yf = np.abs(fft_out[0:int(N//2)])

	fig, axs = plt.subplots(1,1)
	font = {'fontname': 'Apple Chancery'}
	axs.plot(xf, yf)
	axs.set_title('Generated Sound (Frequency Domain)', fontsize=16, **font)
	axs.set_xlabel('frequency', **font)
	axs.set_ylabel('amplitude', **font)
	plt.savefig('audiosite/static/plot.png')
	#plt.show()
	return()
