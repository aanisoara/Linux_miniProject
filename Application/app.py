# Les librairie
import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image

    # IMAGE HERE AFTER TEXTst.subheader("Escolha o valor da posição inicial (em km):")  
    #x0 = st.slider("Escolha entre 3km e 50km",min_value=3.0, max_value=50.0, step = 0.1)  
st.image('https://raw.githubusercontent.com/diakitegaoussou4996/Linux/main/photo.jpg')

#st.image("C:/Users/diaki/Desktop/projet/R.jpeg")
st.title("Application d'admission")
st.subheader("Application réalisée par Anisoara, Eunice, Gaoussou")
st.markdown("***Cette application affiche le resultat***")

#Importation et préparation des  données
def fn():
    df = pd.read_excel('https://query.data.world/s/cud7a5jpgd4t52gc6aajvbn7ulsaqp')
    df2 = pd.read_excel('https://query.data.world/s/bgm5wyxqucb27kofxcae3atheifsds')

    #Suppression des doublons
    df.drop_duplicates(subset ="Application No", keep = 'first', inplace=True)
    df2.drop_duplicates(subset ="Application No", keep = 'first', inplace=True)

    #Jointure des tables
    table=pd.merge(df, df2)


table = pd.read_csv("https://raw.githubusercontent.com/diakitegaoussou4996/Linux/main/adm.csv", sep = ",")
 

#Calcul de la moyenne 
table['FinalMark'] = table[['HighSchool GPA','Physics Marks', 'Chem Marks', 'Biology Marks']].mean(axis=1)

#Variable admission
table['Admit']=np.where(table['FinalMark']>50, 'OUI', 'NON')

#Création d'une nouvelle variable pour l'appréciation du jury
table['Decision'] = [  "\nFelicitations!!! \nVous etes admis! \N{winking face} \n\nLa note de reference choisie par le jury est 50.\
                        \nNous serons heureux de vous accueillir au sein de notre universite a partir du 16 Septembre pour un demarrage effectif des cours" if s>='OUI' else "\nDesole !!\nVous netes pas admis. \n\nLa note de reference choisie par le jury est 50.\
                        Nous vous souhaitons bonne continuation dans vos recherches." for s in table['Admit']]

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
        
        st.write("Ce numéro n'est pas correcte ou n'est disponible dans nos bases des données, veuillez saisir à                    nouveau votre numéro à 4 chiffres")
        
    else:
        st.write('Ce numéro est bien disponible dans nos bases des données')
        st.write(' Votre nom est',  Name_[0])
        st.write("Née le  ", date_nai[0])
        st.write("Admission : ", admit[0])
        st.write(deci[0])
      
        return
    
recherche()
