import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score


# Exercice 1: Nettoyage et exploration des données

def exercice1():  
# Recherche des valeurs manquantes ou incohérentes
    df_cinemas = pd.read_csv(".\csv\salle_de_cinema_ile-de-france.csv", sep=";", encoding="utf-8")

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
    cinemas_data = pd.read_csv(".\csv\salle_de_cinema_ile-de-france.csv", delimiter=";", encoding="utf-8")

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
    cinema_data = pd.read_csv(".\csv\salle_de_cinema_ile-de-france.csv", delimiter=";", encoding="utf-8")

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



# Analyse prédictive et recommandations stratégiques - Exercice 5

# Fonction pour diviser les données des années 2021 et 2022
def analyse_modele():
    data = pd.read_csv(".\csv\salle_de_cinema_ile-de-france.csv", sep=";", encoding="utf-8")

    # Séparation des variables explicatives et cibles pour 2021
    explicatives_2021 = data[['écrans', 'fauteuils', 'population de la commune']]
    cible_2021 = data['entrées 2021']
    print("Données 2021 - Variables explicatives :\n", explicatives_2021.head())
    print("Données 2021 - Variable cible :\n", cible_2021.head())

    # Séparation des variables explicatives et cibles pour 2022
    explicatives_2022 = data[['écrans', 'fauteuils', 'population de la commune']]
    cible_2022 = data['entrées 2022']
    print("Données 2022 - Variables explicatives :\n", explicatives_2022.head())
    print("Données 2022 - Variable cible :\n", cible_2022.head())

    # Jeu d'entraînement et de test
    X = explicatives_2022.values
    Y = cible_2022.values
    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=42)

    # Modèle de régression linéaire
    modele = LinearRegression()
    modele.fit(X_train, Y_train)

    print("Coefficients du modèle :", modele.coef_)
    print("Ordonnée à l'origine :", modele.intercept_)

    # Prédictions et évaluation
    Y_pred = modele.predict(X_test)
    evaluation = pd.DataFrame({'Réel': Y_test, 'Prédit': Y_pred})
    print("Comparaison des valeurs réelles et prédites :\n", evaluation)

    # Indicateurs de performance
    print("Erreur absolue moyenne (MAE) :", mean_absolute_error(Y_test, Y_pred))
    print("Erreur quadratique moyenne (MSE) :", mean_squared_error(Y_test, Y_pred))
    print("Racine de l'erreur quadratique moyenne (RMSE) :", np.sqrt(mean_squared_error(Y_test, Y_pred)))
    print("Coefficient de détermination (R2) :", r2_score(Y_test, Y_pred))


# Recommandations stratégiques basées sur le modèle - Exercice 5
def recommandations():
    def prevoir_entrees(ecrans, fauteuils):
        population = 20000  # population fixe pour la commune
        intercept = -47323.89
        result = (41482.68 * ecrans) + (30.83 * fauteuils) + (-0.19 * population) + intercept
        return result

    print("Prévision pour une commune de 20,000 habitants avec différents scénarios :")
    print("2 écrans, 120 fauteuils :", prevoir_entrees(2, 120))
    print("3 écrans, 120 fauteuils :", prevoir_entrees(3, 120))
    print("2 écrans, 170 fauteuils :", prevoir_entrees(2, 170))


# Programme principal
if __name__ == "__main__":
    print("Bienvenue dans l'analyse des données de CINEMA")
    print("Sélectionnez un exercice parmi les options suivantes :")
    print("""
        1 : Nettoyage des données
        2 : Exploration des données
        3 : Corrélation infrastructures/fréquentation
        4 : Modèle prédictif des entrées annuelles
        5 : Recommandations stratégiques
    """)

    choix = int(input("Entrez le numéro de l'exercice (1 à 5) : "))
    if choix == 1:
        exercice1()
    elif choix == 2:
        analyze_data()
    elif choix == 3:
        analyse_modele()
    elif choix == 4:
        analyse_modele()
    elif choix == 5:
        recommandations()
    else:
        print("Option non valide, merci de réessayer.")
