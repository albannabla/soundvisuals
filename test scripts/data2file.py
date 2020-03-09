
osc1 = "Sine"
osc2 = "Sine"
osc3 = "Sine"
freq1 = 440.0
freq2 = 420.0
freq3 = 500.0

f = open("data.py", "w+")
f.write("osc1 = '%s'\rosc2 = '%s'\rosc3 = '%s'\rfreq1 = %d\rfreq2 = %d\rfreq3 = %d\r" % (osc1, osc2, osc3, freq1, freq2, freq3))
f.close()


