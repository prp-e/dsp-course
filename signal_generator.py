import numpy as np 
from numpy import pi 
import matplotlib.pyplot as plt 

def sine_wave(time, frequency):
    ''' Generates a Sine Wave''' 
    f = frequency 
    t = np.arange(0, time, 0.01)
    wave = np.sin(2 * pi * f * t)

    return wave 

def harmonic_adder(time, frequency, harmonics=15):
    '''Adds harmonics to a sine wave ''' 
    f = frequency
    t = np.arange(0, time, 0.01)

    basic_wave = np.sin(2 * pi * f * t)

    wave = basic_wave 
    count = 2 

    while count < harmonics:
        if count%2 != 0: 
            harmonic = np.sin(2 * pi * count * f * t)/ count 
            wave = wave + harmonic 
        else:
            harmonic = - np.sin(2 * pi * count * f * t)/ count 
            wave = wave + harmonic
        count += 1 
    
    return wave 

time = np.arange(0, 1, 0.0025)
base_wave = sine_wave(4, 1)
resulting_wave = harmonic_adder(4, 1, 100)

plt.figure()
plt.subplot(2, 1, 1)
plt.plot(time, base_wave)
plt.subplot(2, 1, 2)
plt.plot(time, resulting_wave)
plt.savefig("plot.png", dpi=None, facecolor='w', edgecolor='w')