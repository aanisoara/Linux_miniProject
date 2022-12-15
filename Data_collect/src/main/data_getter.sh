
import pandas as pd
import sys

df = pd.read_excel('https://query.data.world/s/cud7a5jpgd4t52gc6aajvbn7ulsaqp')
Data1 = df.to_csv(r'/root/projet_linux/Data_collect/Data1.csv')

df2 = pd.read_excel('https://query.data.world/s/bgm5wyxqucb27kofxcae3atheifsds')
Data2 = df2.to_csv(r'/root/projet_linux/Data_collect/Data2.csv')