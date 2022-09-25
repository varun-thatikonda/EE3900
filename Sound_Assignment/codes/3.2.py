# Plotting x(n) and y(n)

# Name: Ankit Saha
# Roll number: AI21BTECH11004

import numpy as np
import matplotlib.pyplot as plt
import scipy

def x(n):
    if n < 0 or n > 5:
        return 0
    elif n < 4:
        return n + 1
    else:
        return 6 - n

def y(n):
    if n < 0:
        return 0
    else:
        return x(n) + x(n-2) - 0.5 * y(n-1)

vec_x = scipy.vectorize(x, otypes=[float])
vec_y = scipy.vectorize(y, otypes=[float])

N1 = np.linspace(0, 5, 6)
plt.subplot(2, 1, 1)
plt.stem(N1, vec_x(N1))
plt.title('Digital Filter Input-Output')
plt.ylabel('$x(n)$')
plt.grid()

N2 = np.linspace(0, 19, 20)
plt.subplot(2, 1, 2)
plt.stem(N2, vec_y(N2))
plt.xlabel('$n$')
plt.ylabel('$y(n)$')
plt.grid()

plt.savefig('../figs/3.2.png')
plt.show()
