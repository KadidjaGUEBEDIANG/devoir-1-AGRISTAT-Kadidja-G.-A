# -*- coding: utf-8 -*-
"""
Created on Thu Feb 13 17:06:23 2025

@author: GANK
"""

#DEVOIR 1 DE STATISTIQUE AGRICOLE
# Réalisé par Kadidja GUEBEDIANG A NKEN

##Préparation des données

####Spécifier le répertoire de travail
import os
os.chdir("C:/Users/LENOVO/Downloads")

####Importer la base de données `household_data.csv`.
import pandas as pd
df_households = pd.read_csv("household_data.csv")

### Afficher le nombre d'observations et de variables.
print("Le nombre d'observations est ", len(df_households)," et le nombre de variable ", len(df_households.columns))


## Calculs et analyses

#### Calculer la superficie moyenne par ménage dans chaque village.
superficie_moyenne = df_households.groupby("village")["area_maize"].mean().reset_index()

    # Renommer la colonne pour plus de clarté
superficie_moyenne.columns = ["village", "Superficie_Moyenne"]
print(superficie_moyenne)

#### Calcul du rendement moyen
    df_households["rdt_maize"] = df_households["prod_maize"] / df_households["area_maize"]
    rendement_moyen = df_households["rdt_maize"].mean()
    print(f"Rendement moyen du maïs : {rendement_moyen:.2f}")

#### Comparaison par sexe
    rendement_par_sexe = df_households.groupby("hhsex")["rdt_maize"].mean()
    print(rendement_par_sexe)

#### Corrélation âge-rendement
    correlation_age_rendement = df_households["hhage"].corr(df_households["rdt_maize"])
    print(f"Corrélation entre âge et rendement du maïs : {correlation_age_rendement:.3f}")

#### Aggréger la base au niveau village, de sorte à avoir le même format que la base kawteef.xlsx

df_agg = df_households.groupby("village").agg({
    "hhsize": "sum",
    "prod_maize": "sum",
    "area_maize": "sum",
}).reset_index()

print(df_agg.head())

#### Quelle la superficie totale emblavée dans la Zone A (villages : 2, 7, 13, 47, 38) ?
zone_A_villages = [2, 7, 13, 47, 38]
superficie_zone_A = df_households[df_households["village"].isin(zone_A_villages)]["area_maize"].sum()
print(f"Superficie totale emblavée dans la Zone A : {superficie_zone_A:.3f} ha")

####Calculer la production totale dans la Zone A.
production_zone_A = df_households[df_households["village"].isin(zone_A_villages)]["prod_maize"].sum()
print(f"Production totale dans la Zone A : {production_zone_A:.2f} kg")

####Calculer le rendement moyen du maïs dans chaque zone.
rendement_par_village = df_households.groupby("village")["rdt_maize"].mean()
print(rendement_par_village)

#### Créer une variable `Subvention` pour indiquer si un village a un rendement de moins de 500kg/ha.
df_households["Subvention"] = df_households["rdt_maize"] < 500
print(df_households[["village","rdt_maize","Subvention"]])

#8. Conserver uniquement les villages où la superficie moyenne par ménage est < 1 hectare et enregistrer sous `pauvres_villages.csv`.
df__households = pd.read_csv("household_data.csv")
pauvres_villages = df__households.groupby('village')['area_maize'].mean()
pauvres_villages = pauvres_villages[pauvres_villages < 1]
pauvres_villages.to_csv("pauvres_villages.csv", index=False)

#9. Calculer la taille moyenne par zone et exporter sur word et excel.
