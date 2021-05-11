import numpy as np
import matplotlib.pyplot as plt

x1 = np.arange(0., 30., 0.1)

s1 = np.sin(x1)
c = np.cos(x1)
s2 = np.sin(-x1)
s3 = s1+2

plt.subplot(2, 1, 1)
plt.plot(x1, s1, label='sin(x)')
plt.plot(x1, c, label='cos(x)')
plt.subplot(2, 1, 2)
plt.plot(x1, s3, label='sin(x)')
plt.plot(x1, s2, label='sin(x)')
plt.legend()
plt.show()