import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score


# Exercice 1: Nettoyage et exploration des données

def exercice1():  
# Recherche des valeurs manquantes ou incohérentes
    df_cinemas = pd.read_csv("./data/cinemas.csv", sep=";", encoding="utf-8")

    print("Valeurs manquantes ou incohérentes selon les différents champs de cinemas.csv:")
    print(df_cinemas.isnull().sum())

# Affichage des colonnes ayant des valeurs manquantes ou incohérentes
    colonnes_en_defaut = [
        'label Art et Essai',
        'programmateur', 
        'évolution entrées', 
        'entrées 2021'
    ]

    print("Avant traitement des colonnes en défaut:")
    print(df_cinemas[colonnes_en_defaut])


# Traitement des colonnes en défaut
    df_cinemas = df_cinemas.fillna({
        'label Art et Essai': 'Non renseigné',
        'programmateur': 'Non renseigné',
        'évolution entrées': 0,
        'entrées 2021': 0
    })

# Affichage des colonnes ayant des valeurs manquantes ou incohérentes
    print("Après traitement des colonnes en défaut:")
    print(df_cinemas[colonnes_en_defaut])


# Affichage des premières lignes du dataset :
    print("Premières lignes du fichier cinemas.csv:")
    print(df_cinemas.head())

#Affichage des statistiques descriptives des colonnes numériques principales
    cinemas_filter = [
        'fauteuils',
        'écrans',
        'entrées 2022',
        'entrées 2021'
    ]

    print("Colonnes principales du fichier cinemas.csv:")
    print(df_cinemas[cinemas_filter])


# Analyse des données - Exercice 2

def analyze_data():
    # Chargement des données
    cinemas_data = pd.read_csv("./data/cinemas.csv", delimiter=";", encoding="utf-8")

    # Calcul des totaux des entrées et des fauteuils par commune
    aggregated_data = cinemas_data.groupby('commune')[['entrées 2022', 'fauteuils']].sum()

    # Calcul des entrées moyennes par fauteuil
    avg_entries_per_seat = aggregated_data['entrées 2022'] / aggregated_data['fauteuils']

    print("Analyse : Moyenne des entrées par fauteuil pour chaque région (2022)")
    print(avg_entries_per_seat)

    # Top 3 des communes avec le plus d'entrées moyennes par fauteuil
    top_3_communes = avg_entries_per_seat.sort_values(ascending=False).head(3)
    print("\nTop 3 des communes avec le plus d'entrées moyennes par fauteuil :")
    print(top_3_communes)

    # Bottom 3 des communes avec le moins d'entrées moyennes par fauteuil
    bottom_3_communes = avg_entries_per_seat.sort_values().head(3)
    print("\nBottom 3 des communes avec le moins d'entrées moyennes par fauteuil :")
    print(bottom_3_communes)

    # Diagramme des 10 communes avec le plus d'entrées moyennes par fauteuil
    top_10_communes = avg_entries_per_seat.sort_values(ascending=False).head(10).reset_index()
    top_10_communes.columns = ['commune', 'avg_entries_per_seat']

    top_10_communes.set_index('commune')['avg_entries_per_seat'].plot(
        kind='bar', figsize=(14, 6), color='skyblue'
    )
    plt.title("Top 10 : Moyenne des entrées par fauteuil (2022)")
    plt.ylabel('Entrées moyennes par fauteuil')
    plt.xlabel('Communes')
    plt.xticks(rotation=45)
    plt.grid(axis='y')
    plt.show()

    # Diagramme des 10 communes avec le moins d'entrées moyennes par fauteuil
    bottom_10_communes = avg_entries_per_seat.sort_values().head(10).reset_index()
    bottom_10_communes.columns = ['commune', 'avg_entries_per_seat']

    bottom_10_communes.set_index('commune')['avg_entries_per_seat'].plot(
        kind='bar', figsize=(14, 6), color='salmon'
    )
    plt.title("Bottom 10 : Moyenne des entrées par fauteuil (2022)")
    plt.ylabel('Entrées moyennes par fauteuil')
    plt.xlabel('Communes')
    plt.xticks(rotation=45)
    plt.grid(axis='y')
    plt.show()
