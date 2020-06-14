import numpy as np
from numpy import pi 
class Signal:
    """ Generates a signal """ 
    def __init__(self, frequency, time, harmonics=50):
        """ Initializing the signal """
        self.frequency = frequency
        self.time = np.arange(0, time, 0.01)
        self.harmonics = harmonics
    def sine_wave(self):
        """Creates a Sign Wave""" 
        wave = np.sin(2 * pi * self.frequency * self.time)
        return wave 
    def sawtooth_wave(self):
        """ Creates a Sawtooth Wave """ 
        basic_wave = self.sine_wave()
        wave = basic_wave 
        count = 2 
        while count < self.harmonics:
            if count%2 != 0: 
                harmonic = np.sin(2 * pi * count * self.frequency * self.time)/ count 
                wave = wave + harmonic 
            else:
                harmonic = - np.sin(2 * pi * count * self.frequency * self.time)/ count 
                wave = wave + harmonic
            count += 1 
        return wave
    def reverse_sawtooth_wave(self):
        """ Creates a Reverse Sawtooth Wave """ 
        basic_wave = self.sine_wave()
        wave = basic_wave 
        count = 2 
        while count < self.harmonics:
            if count%2 != 0: 
                harmonic = np.sin(2 * pi * count * self.frequency * self.time)/ count 
                wave = wave + harmonic 
            else:
                harmonic = np.sin(2 * pi * count * self.frequency * self.time)/ count 
                wave = wave + harmonic
            count += 1 
        return wave
    def square_wave(self):
        """ Creates a Square Wave """ 
        basic_wave = self.sine_wave()
        wave = basic_wave 
        count = 2 
        while count < self.harmonics:
            if count%2 != 0:
                harmonic = np.sin(2 * pi * count * self.frequency * self.time)/ count 
                wave = wave + harmonic
            count += 1 
        return wave
    def triangle_wave(self):
        """ Creates a Triangle Wave """ 
        basic_wave = - np.cos(2 * pi * self.frequency * self.time)
        wave = basic_wave 
        count = 2 
        while count < self.harmonics:
            if count%2 != 0:
                harmonic = -np.cos(2 * pi * count * self.frequency * self.time)/ count ** 2
                wave = wave + harmonic
            count += 1  
        return wave
