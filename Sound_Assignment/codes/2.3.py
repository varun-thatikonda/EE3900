
import soundfile as sf
from scipy import signal
input_signal, fs = sf.read('Sound_Noise.wav') 
sampl_freq = fs
order = 10
cutoff_freq = 3000.0  
Wn = 2 * cutoff_freq / sampl_freq  
b, a = signal.butter(order, Wn, 'low') 
output_signal = signal.filtfilt(b, a, input_signal)
sf.write('Sound_With_Reduced_Noise.wav', output_signal, fs) 
