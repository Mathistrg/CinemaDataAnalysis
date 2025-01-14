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


# Analyse de la corrélation entre infrastructures et fréquentation - Exercice 3

def analyze_correlation():
    # Lecture des données
    cinema_data = pd.read_csv("./data/cinemas.csv", delimiter=";", encoding="utf-8")

    # Corrélation entre le nombre d'écrans et les entrées de 2022
    screens = cinema_data['écrans'].tolist()
    annual_entries = cinema_data['entrées 2022'].tolist()
    n_screens = len(screens)

    sum_screens = sum(screens)
    sum_entries = sum(annual_entries)
    sum_products_screen = sum(x * y for x, y in zip(screens, annual_entries))
    sum_squares_screens = sum(x ** 2 for x in screens)

    numerator_screens = (n_screens * sum_products_screen) - (sum_screens * sum_entries)
    denominator_screens = ((n_screens * sum_squares_screens - sum_screens ** 2) *
                           (n_screens * sum_entries - sum_entries ** 2)) ** 0.5

    correlation_screens_entries = numerator_screens / denominator_screens if denominator_screens != 0 else 0
    print("Corrélation entre le nombre d'écrans et les entrées de 2022 :")
    print(correlation_screens_entries)

    # Corrélation entre le nombre de fauteuils et les entrées de 2022
    seats = cinema_data['fauteuils'].tolist()
    n_seats = len(seats)

    sum_seats = sum(seats)
    sum_products_seats = sum(x * y for x, y in zip(seats, annual_entries))
    sum_squares_seats = sum(x ** 2 for x in seats)

    numerator_seats = (n_seats * sum_products_seats) - (sum_seats * sum_entries)
    denominator_seats = ((n_seats * sum_squares_seats - sum_seats ** 2) *
                         (n_seats * sum_entries - sum_entries ** 2)) ** 0.5

    correlation_seats_entries = numerator_seats / denominator_seats if denominator_seats != 0 else 0
    print("Corrélation entre le nombre de fauteuils et les entrées de 2022 :")
    print(correlation_seats_entries)

    # Nuage de points : nombre d'écrans vs entrées de 2022
    x_screens = cinema_data['écrans']
    y_entries = cinema_data['entrées 2022']
    slope_screens = ((x_screens * y_entries).mean() - x_screens.mean() * y_entries.mean()) / \
                    ((x_screens ** 2).mean() - (x_screens.mean() ** 2))
    intercept_screens = y_entries.mean() - slope_screens * x_screens.mean()

    plt.scatter(x_screens, y_entries, color='blue', label='Données')
    plt.plot(x_screens, slope_screens * x_screens + intercept_screens, color='orange', label='Régression linéaire')
    plt.title("Corrélation : Nombre d'écrans vs Entrées annuelles (2022)")
    plt.xlabel("Nombre d'écrans")
    plt.ylabel("Entrées annuelles")
    plt.legend()
    plt.grid()
    plt.show()

    # Nuage de points : nombre de fauteuils vs entrées de 2022
    x_seats = cinema_data['fauteuils']
    slope_seats = ((x_seats * y_entries).mean() - x_seats.mean() * y_entries.mean()) / \
                  ((x_seats ** 2).mean() - (x_seats.mean() ** 2))
    intercept_seats = y_entries.mean() - slope_seats * x_seats.mean()

    plt.scatter(x_seats, y_entries, color='green', label='Données')
    plt.plot(x_seats, slope_seats * x_seats + intercept_seats, color='red', label='Régression linéaire')
    plt.title("Corrélation : Nombre de fauteuils vs Entrées annuelles (2022)")
    plt.xlabel("Nombre de fauteuils")
    plt.ylabel("Entrées annuelles")
    plt.legend()
    plt.grid()
    plt.show()
