

import numpy as np
import sys
import streamlit as st
import pandas as pd
from PIL import Image
    


st.sidebar.title("Application")
    
image = Image.open('Image.jpg')
st.image(image, caption='Admission')

st.title("Application d'admission")
st.subheader("Application: ADMIT")
st.markdown("***Cette application affiche le resultat***")


data1 = pd.read_csv(r'~/Data_collect/Data1.csv')
data2 = pd.read_csv(r'~/Data_collect/Data2.csv')

table = pd.merge(data1, data2)

table.drop_duplicates(subset ="Application No", keep = 'first', inplace=True)

table['FinalMark'] = table[['HighSchool GPA','Physics Marks', 'Chem Marks', 'Biology Marks']].mean(axis=1)
table['Admit']=np.where(table['FinalMark']>50, 'OUI', 'NON')

table["Application No"]=table["Application No"].astype(str)
table['Decision'] = ["Felicitation, vous etes admis" if s=='OUI' else "Desole, vous n'etes pas admis pour cette cesson" for s in table['Admit']]
table["Application No"]=table["Application No"].astype(str)


def recherche():

    Recherche = st.text_input("Veuillez saisir votre numero/Application NO):").title()
    Resultat = st.button("Appuyez pour voir votre resultat ")

    Numero= table["Application No"].tolist()          
    Name_ = table[table["Application No"].str.contains(Recherche)].loc[:,'Name'].tolist()
    date_nai = table[table["Application No"].str.contains(Recherche)].loc[:,'DOB'].tolist()
    admit = table[table["Application No"].str.contains(Recherche)].loc[:,'Admit'].tolist()
    deci = table[table["Application No"].str.contains(Recherche)].loc[:,'Decision'].tolist()


    if Recherche=='':
        
        st.write("")
    elif Recherche not in Numero:
        
        st.write("Ce numero n'est pas correcte ou n'est disponible dans nos bases des donnees, veuillez saisir a nouveau votre numero a 4 chiffre")
        
    else:
        st.write('Ce numero est bien disponible dans nos bases des donnees')
        st.write('Votre nom est',  Name_[0])
        st.write("Nee le  ", date_nai[0])
        st.write("Admission : ", admit[0])
        st.write(deci[0])
      
        return
    
recherche()

