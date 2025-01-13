import pandas as pd

try:
    infrastructure = pd.read_csv('C:\TRAVAIL\VS CODE\PYTHON OD\csv\salle_de_cinema_ile-de-france.csv')
    entree_annuelle = pd.read_csv('C:\TRAVAIL\VS CODE\PYTHON OD\csv\salle_de_cinema_ile-de-france.csv')
except FileNotFoundError as e:
    print(f"Erreur : {e}")
    exit()

def clean_data(df):
    print("\nValeurs manquantes avant nettoyage :")
    print(df.isna().sum())

    df = df.dropna(subset=['Nom', 'Date'])

    if 'Capacité' in df.columns:
        df['Capacité'] = df['Capacité'].fillna(0)

    if 'Capacité' in df.columns:
        df = df[df['Capacité'] >= 0]

    df = df.drop_duplicates()

    print("\nValeurs manquantes après nettoyage :")
    print(df.isna().sum())

    return df

infrastructure = clean_data(infrastructure)
entree_annuelle = clean_data(entree_annuelle)

print("\nDonnées de 'infrastructure' après nettoyage :")
print(infrastructure)

print("\nDonnées de 'entree_annuelle' après nettoyage :")
print(entree_annuelle)

infrastructure.to_csv('infrastructure_cleaned.csv', index=False)
entree_annuelle.to_csv('entree_annuelle_cleaned.csv', index=False)
