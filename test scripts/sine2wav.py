##this routine will generate and save a sine sound to a .wav file
### note: it requires installation of sounddevice and soundfile modules



from __future__ import division
import numpy as np
import sounddevice as sd
import soundfile as sf

volume = 0.5  # range [0.0, 1.0]
fs = 44100  # sampling rate, Hz
duration = 2.0  # in seconds
f = 440.0  # sine frequency, Hz

t = np.arange(int(duration * fs)) / fs
samples = volume * np.sin(2 * np.pi * f * t)

sf.write('myfile.wav', samples, fs, subtype='PCM_24')

sd.play(samples, fs)
sd.wait()