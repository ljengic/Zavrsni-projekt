#!/usr/bin/python

import pandas as pd
import matplotlib.pyplot as plt

plt.rcParams["figure.figsize"] = [7.50, 3.50]
plt.rcParams["figure.autolayout"] = True

headers = ['Utilization', 'BWP','RTO']

df = pd.read_csv('BWP.csv', names=headers)

df.set_index('Utilization').plot()

plt.show()
