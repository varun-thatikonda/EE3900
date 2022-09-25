
import numpy as np
import matplotlib.pyplot as plt

def H1(z):
    return (1 + z**-2) / (1 + 0.5*(z**-1))

def H2(w):
    return 4*np.abs(np.cos(w)) / np.sqrt(5 + 4*np.cos(w))

Omega1 = np.linspace(-3.5*np.pi, 3.5*np.pi, 80)
Omega2 = np.linspace(-3.5*np.pi, 3.5*np.pi, 500)

plt.plot(Omega2, H2(Omega2), label='$\\frac{4|\cos\omega|}{\sqrt{5 + 4\cos\omega}}$')
plt.plot(Omega1, np.abs(H1(np.exp(1j * Omega1))), 'o', label='$\\frac{|1 + e^{-2\jmath\omega}|}{|1 + \\frac{1}{2} e^{-\jmath\omega}|}$')
plt.title('Filter Frequency Response')
plt.xlabel('$\omega$')
plt.ylabel('$|H(e^{\jmath\omega})| $')
plt.grid()
plt.legend(loc='upper right')
plt.savefig('../figs/4.5.png')
plt.show()
