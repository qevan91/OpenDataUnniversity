import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Charger le fichier CSV
data = pd.read_csv("trafic_moyen_journalier_sur_reseau_routier.csv",on_bad_lines='skip',sep='\t',quotechar='"',)

# Agréger les données par année
try:
    grouped_tmja = data.groupby('anneeMesureTrafic')['TMJA'].mean().reset_index()
    print("Données regroupées par année :")
    print(grouped_tmja)
except Exception as e:
    print(f"Erreur lors de l'agrégation des données : {e}")
    exit()

# Tracé de la courbe
try:
    plt.figure(figsize=(12, 6))
    sns.barplot(x='anneeMesureTrafic', y='TMJA', data=grouped_tmja, palette="Blues_d")
    plt.title('Évolution du TMJA par Année')
    plt.xlabel('Année')
    plt.ylabel('TMJA Moyen')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()
except Exception as e:
    print(f"Erreur lors du tracé de la courbe : {e}")

