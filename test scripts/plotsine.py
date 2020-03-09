##this routine will plot a sine using plotly


import numpy as np
import plotly.graph_objects as go

fs = 44100  # sampling rate, Hz
duration = 0.01  # in seconds
f_1 = 440.0  # frequency, Hz
f_2 = 400.0  # frequency, Hz
f_3 = 470.0  # frequency, Hz
t = np.arange(int(duration * fs)) / fs
osc = np.sin(2 * np.pi * f_1 * t)

fig = go.Figure(data=go.Scatter(x=t, y=osc))
fig.show()


