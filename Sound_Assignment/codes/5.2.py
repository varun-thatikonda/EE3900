
import numpy as np
import matplotlib.pyplot as plt
import scipy

def u(n):
    if n >= 0:
        return 1
    else:
        return 0

def h(n):
    return u(n) * (-0.5)**n + u(n-2) * (-0.5)**(n-2) 


vec_h = scipy.vectorize(h, otypes=[float])

N = np.linspace(0, 19, 20)
plt.stem(N, vec_h(N))
plt.xlabel('$n$')
plt.ylabel('$h(n)$')
plt.grid()
plt.title('Filter Impulse Response')
plt.savefig('../figs/5.2.png')
plt.show()
