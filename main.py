import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(1, 20)
plt.plot(x, 1/x, label='1/x')

plt.xlabel('x')
plt.ylabel('f(x)')

plt.xlim([0, 20])
plt.ylim([0, 1])

plt.legend()
plt.show()
