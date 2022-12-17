
import pandas as pd
import sys

df = pd.read_excel('https://query.data.world/s/cud7a5jpgd4t52gc6aajvbn7ulsaqp')

df2 = pd.read_excel('https://query.data.world/s/bgm5wyxqucb27kofxcae3atheifsds')

Data1 = df.to_csv(r'~/Projets_1_Master2/Data_collect/Data1.csv')

Data2 = df2.to_csv(r'~/Projets_1_Master2/Data_collect/Data2.csv')

