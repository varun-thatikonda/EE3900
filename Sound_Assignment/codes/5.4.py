
import numpy as np
import matplotlib.pyplot as plt
import scipy

def delta(n):
    if n == 0:
        return 1
    else:
        return 0

def h(n):
    if n == 0:
        return 1
    else:
        return delta(n) + delta(n-2) - 0.5*h(n-1)

vec_h = scipy.vectorize(h, otypes=[float])

N = np.linspace(0, 19, 20)
plt.stem(N, vec_h(N))
plt.xlabel('$n$')
plt.ylabel('$h(n)$')
plt.grid()
plt.title('Impulse Response Definition')
plt.savefig('../figs/5.4.png')
plt.show()
