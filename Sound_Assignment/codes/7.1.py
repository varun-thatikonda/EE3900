
import soundfile as sf
from scipy import signal
import numpy as np
input_signal, fs = sf.read('Sound_Noise.wav') 

sampl_freq = fs
print(sampl_freq)

order = 4   

cutoff_freq = 4000.0  

Wn = 2 * cutoff_freq / sampl_freq  

b, a = signal.butter(order, Wn, 'low') 
print(b)
print(a)

N = len(input_signal)
k = np.arange(N)

X = np.fft.fft(input_signal)

num = np.polyval(b, np.exp(-2j * np.pi * k / N))
den = np.polyval(a, np.exp(-2j * np.pi * k / N))
H = num / den

Y = X * H
y = np.fft.ifft(Y)

output_signal = np.real(y)
print(output_signal)

sf.write('7.1.wav', output_signal, fs) 
