import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt

pd.options.display.max_rows = 9999


df = pd.read_csv('data.csv')
print(df.info())


new_df = df.dropna()
print(new_df.info())
#print(new_df)

df.plot()
plt.show()
