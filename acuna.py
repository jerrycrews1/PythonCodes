import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('acuna.csv')

bavg = df.groupby('Pos').BA.mean().reset_index()

max_bavg = bavg.BA.max()
# print(max_bavg)

plt.bar(bavg.Pos, bavg.BA)
plt.ylim(bottom=.250, top=.300)
plt.show()
