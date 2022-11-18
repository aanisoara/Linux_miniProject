
import pandas as pd
import sys

df2 = pd.read_excel('https://query.data.world/s/bgm5wyxqucb27kofxcae3atheifsds')

Data2 = df2.to_csv(r'/root/projet_linux/Data_collect/Data2.csv')