# Les librairie
import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image

st.image('https://raw.githubusercontent.com/aanisoara/Projets_1_Master2/master/Application/photo.jpg')

st.title("Application ADMIT")
st.subheader("Application réalisée par Anisoara, Eunice et Gaoussou")
st.markdown("***Cette application affiche le résultat***")

#Importation de la table 
table = pd.read_csv("https://raw.githubusercontent.com/aanisoara/Projets_1_Master2/master/Application/adm.csv.xls", sep = ",")
 

#Calcul de la moyenne 
table['FinalMark'] = table[['HighSchool GPA','Physics Marks', 'Chem Marks', 'Biology Marks']].mean(axis=1)

#Variable admission
table['Admit']=np.where(table['FinalMark']>50, 'OUI', 'NON')

#Création d'une nouvelle variable pour l'appréciation du jury
table['Decision'] = ["\nFélicitations!!! \nVous êtes admis! \N{winking face} \n\nLa note de référence choisie par le jury est 50.\nNous serons heureux de vous accueillir au sein de notre Université. " if s == 'OUI' else "Désolé, vous n'êtes pas admis. \n\nLa note de référence choisie par le jury est 50. \n \nNous vous souhaitons bonne continuation dans vos rechérches. \n" for s in table['Admit']]

#Transformation de la variable Application en objet
table["Application No"]=table["Application No"].astype(str)

def recherche():

    Recherche = st.text_input("Veuillez saisir votre numéro/Application NO):").title()
    Resultat = st.button("Appuyez pour voir votre résultat ")

    Numero= table["Application No"].tolist()          
    Name_ = table[table["Application No"].str.contains(Recherche)].loc[:,'Name'].tolist()
    date_nai = table[table["Application No"].str.contains(Recherche)].loc[:,'DOB'].tolist()
    admit = table[table["Application No"].str.contains(Recherche)].loc[:,'Admit'].tolist()
    deci = table[table["Application No"].str.contains(Recherche)].loc[:,'Decision'].tolist()


    if Recherche=='':
        
        st.write("")
    elif Recherche not in Numero:
        
        st.write("Ce numéro n'est pas correct ou est indisponible dans nos bases des données, veuillez saisir à nouveau votre numéro à 4 chiffres")
        
    else:
        st.write('Votre nom est : ',  Name_[0])
        st.write("Née le : ", date_nai[0])
        st.write("Admission : ", admit[0])
        st.write(deci[0])
      
        return
    
recherche()
