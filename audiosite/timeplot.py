
import numpy as np
from scipy import signal
from scipy.fftpack import fft
import matplotlib.pyplot as plt

#fixed values
volume = 0.5  # range [0.0, 1.0]
fs = 44100  # sampling rate, Hz
duration = 2.0  # in seconds


#variables on input
#freq1 = 440.0  # frequency, Hz
#freq2 = 400.0  # frequency, Hz
#freq3 = 470.0  # frequency, Hz
#osc1 = "saw"
#osc2 = "sine"
#osc3 = "sine"

def timeplot(freq1,osc1,freq2,osc2,freq3,osc3):
	period = 1/freq1
	t = np.arange(int(period * 30 * fs)) / fs

	if osc1 == "Sawtooth":
		out1 = signal.sawtooth(2 * np.pi * freq1 * t)
	elif osc1 == "Square":
		out1 = signal.square(2 * np.pi * freq1 * t)
	else: 
		out1 = np.sin(2 * np.pi * freq1 * t)

	if osc2 == "Sawtooth":
		out2 = signal.sawtooth(2 * np.pi * freq2 * t)
	elif osc2 == "Square":
		out2 = signal.square(2 * np.pi * freq2 * t)
	else: 
		out2 = np.sin(2 * np.pi * freq2 * t)

	if osc3 == "Sawtooth":
		out3 = signal.sawtooth(2 * np.pi * freq3 * t)
	elif osc3 == "Square":
		out3 = signal.square(2 * np.pi * freq3 * t)
	else: 
		out3 = np.sin(2 * np.pi * freq3 * t)
	samples = volume * (out1 + out2 + out3)
	fig, axs = plt.subplots(1,1)
	axs.plot(t, samples)
	axs.set_title('Time Signal of the Generated Sound', fontsize=16)
	axs.set_xlabel('time')
	axs.set_ylabel('amplitude')
	plt.savefig('audiosite/static/chart.png')
	#graph =	plt.show()
	return()
