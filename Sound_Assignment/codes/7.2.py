# Reducing noise in an audio file

import soundfile as sf
from scipy import signal
import numpy as np
import matplotlib.pyplot as plt

input_signal, fs = sf.read('Sound_Noise.wav') 

sampl_freq = fs

order = 4   

cutoff_freq = 4000.0  

Wn = 2 * cutoff_freq / sampl_freq  

b, a = signal.butter(order, Wn, 'low') 

N = len(input_signal)
k = np.arange(N)

X = np.fft.fft(input_signal)

num = np.polyval(b, np.exp(-2j * np.pi * k / N))
den = np.polyval(a, np.exp(-2j * np.pi * k / N))
H = np.abs(num / den)

Y = X * H
y = np.fft.ifft(Y)
output_signal = np.real(y)

# Plotting y(n)
plt.stem(k[:100], output_signal[:100])
plt.title('Filter Output')
plt.xlabel('$n$')
plt.ylabel('$y(n)$')
plt.grid()
plt.savefig('../figs/7.2.1.png')
plt.show()

Omega = np.linspace(-3*np.pi, 3*np.pi, 200)
filter_frequency = np.abs(np.polyval(b, np.exp(1j * Omega)) / np.polyval(a, np.exp(1j * Omega)))

# Plotting |H(e^jw)|
plt.plot(Omega, filter_frequency)
plt.title('Filter Frequency Response')
plt.xlabel('$\omega$')
plt.ylabel('$|H(e^{\jmath \omega})|$')
plt.grid()
plt.savefig('../figs/7.2.2.png')
plt.show()

filter_impulse = np.real(np.fft.ifft(H))

# Plotting h(n)
plt.stem(k[:50], filter_impulse[:50])
plt.title('Filter Impulse Response')
plt.xlabel('$n$')
plt.ylabel('$h(n)$')
plt.grid()
plt.savefig('../figs/7.2.3.png')
plt.show()

# Theoretical h(n)
r, p, k = signal.residuez(b, a)
print(r, '\n', p, '\n', k)
