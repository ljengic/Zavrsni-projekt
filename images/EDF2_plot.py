#!/usr/bin/python

import pandas as pd
import matplotlib.pyplot as plt

plt.rcParams["figure.figsize"] = [7.50, 3.50]
plt.rcParams["figure.autolayout"] = True

headers = ['Utilization', 'EDF','RTO','BWP']

df = pd.read_csv('EDF2_v2.csv', names=headers)

df.set_index('Utilization').plot()

plt.xlabel('Faktor opterećenja')
plt.ylabel('Postotak poslova na kojima su prekršeni postavljeni uvjeti')

plt.xlim(0.85,1.55)
plt.ylim(0,10)

f = plt.figure()
f.set_figwidth(4)
f.set_figheight(4)

plt.show()
