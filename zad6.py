import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_excel('imiona.xlsx')

aM = df[df.Plec == 'M']
aK = df[df.Plec == 'K']
aM = aM.groupby(['Rok']).Liczba.sum().reset_index()
aK = aK.groupby(['Rok']).Liczba.sum().reset_index()

b = df.groupby(['Rok']).Liczba.sum().reset_index()

plt.subplot(1, 3, 1)
plt.bar(df.Plec, df.Liczba)

plt.subplot(1, 3, 2)
plt.plot(aM.Rok, aM.Liczba, label='M')
plt.plot(aK.Rok, aK.Liczba, label='K')
plt.legend()

plt.subplot(1, 3, 3)
plt.bar(b.Rok, b.Liczba)

plt.show()
