##this routine will show and save a plot into a file

## WORK IN PROGRESS

import numpy as np
import matplotlib.pyplot as plt

fs = 44100  # sampling rate, Hz
duration = 0.01  # in seconds
f_1 = 440.0  # frequency, Hz
f_2 = 400.0  # frequency, Hz
f_3 = 470.0  # frequency, Hz
t = np.arange(int(duration * fs)) / fs
osc = np.sin(2 * np.pi * f_3 * t)

plt.plot(osc)
plt.savefig('plot.png')
#plt.show()


