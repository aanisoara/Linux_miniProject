import pandas as pd
import numpy as np
import sys


data1 = pd.read_csv(r'~/Projets_1_Master2/Data_collect/Data1.csv')
data2 = pd.read_csv(r'~/Projets_1_Master2/Data_collect/Data2.csv')

table = pd.merge(data1, data2)

table.drop_duplicates(subset ="Application No", keep = 'first', inplace=True)

table['FinalMark'] = table[['HighSchool GPA','Physics Marks', 'Chem Marks', 'Biology Marks']].mean(axis=1)
table['Admit']=np.where(table['FinalMark']>50, 'OUI', 'NON')

table["Application No"]=table["Application No"].astype(str)


table['Decision']=["\nFelicitations!!! \nVous etes admis! \N{winking face} \n\nLa note de reference choisie par le jury est 50.\nNous serons heureux de vous accueillir au sein de notre Universite. " if s == 'OUI' else "Desole, vous n'etes pas admis. \n\nLa note de reference choisie par le jury est 50. \n \nNous vous souhaitons bonne continuation dans vos recherches. \n" for s in table['Admit']]

table["Application No"]=table["Application No"].astype(str)

Recherche=sys.argv[1]
def recherche(Recherche):

    Name_ = table[table["Application No"].str.contains(Recherche)].loc[:,'Name'].tolist()
    Numero= table["Application No"].tolist()          
    date_nai = table[table["Application No"].str.contains(Recherche)].loc[:,'DOB'].tolist()
    admit = table[table["Application No"].str.contains(Recherche)].loc[:,'Admit'].tolist()
    deci = table[table["Application No"].str.contains(Recherche)].loc[:,'Decision'].tolist()
    mean = table[table["Application No"].str.contains(Recherche)].loc[:,'FinalMark'].tolist()

    if Recherche=='':
        print("")
    elif Recherche not in Numero:
        print("\nLe numero saisi est incorrect. Veuillez saisir a nouveau votre numero de candidature: \n")
    else:
        print('\nVotre nom est: ',  Name_[0])
        print("\nDate de naissance: ", date_nai[0])
        print('\nLa moyenne obtenue est: ',mean[0])
        print("\nAdmission: ", admit[0])
        print(deci[0])
        
      
        return
    
recherche(Recherche)
