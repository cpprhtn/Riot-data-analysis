import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import matplotlib as mpl
import seaborn as sns

plt.rc('font', family='AppleGothic')


df = pd.read_csv('faker_total_df.csv')

df['KDA'] = (df['kills'] + df['assists']) / df['deaths']

average_kda = df.groupby('champion')['KDA'].mean().reset_index()\

average_kda.plot(x='champion', y='KDA', kind='bar', figsize=(20, 10), rot=0)
plt.show()