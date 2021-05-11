import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('zamowienia.csv', header=0, sep=';', decimal='.')
a = df.groupby(['Sprzedawca']).Utarg.sum().reset_index()
explode = (0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1)
plt.pie(a.Utarg, explode=explode, labels=a.Sprzedawca, autopct=lambda pct: '{:.1f}%'.format(pct), shadow=True)

plt.show()