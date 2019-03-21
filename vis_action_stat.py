import pandas as pd
from matplotlib import pyplot as plt
import numpy as np

df = pd.read_csv('data.csv')
columns = df.columns

xlabels = [x.split("_")[0] for x in columns[0:-1]]
x = np.arange(len(xlabels))

for i in range(len(df)):
    line = list(df.ix[i])[0:-1]
    y = np.array(line)
    # print(y)
    plt.plot(x,y)
plt.xticks(x,xlabels,rotation=-60)
plt.show()

