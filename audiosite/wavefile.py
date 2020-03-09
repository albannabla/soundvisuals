
import soundfile as sf
import numpy as np
from scipy import signal

volume = 0.5  # range [0.0, 1.0]
fs = 44100  # sampling rate, Hz
duration = 2.0  # in seconds
N = duration * fs 

def render(freq1,osc1,freq2,osc2,freq3,osc3):
	t = np.arange(int(N)) / fs

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
	sf.write('audiosite/static/audio.wav', samples, fs, subtype='PCM_24')
	return()
