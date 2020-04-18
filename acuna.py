import requests
import re
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('acuna.csv')

bavg = df.groupby('Pos').BA.mean().reset_index()
print(bavg)

max_bavg = bavg.BA.max()

# print(max_bavg)

# bavg.plot(x='Pos', y='BA', kind='bar').lim(2.50,3.00)
# plt.show()

plt.bar(bavg.Pos, bavg.BA)

plt.ylim(bottom=.250, top=.300)

plt.show()
