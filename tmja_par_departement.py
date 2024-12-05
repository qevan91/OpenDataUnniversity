import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


data = pd.read_csv("trafic_moyen_journalier_sur_reseau_routier.csv",on_bad_lines='skip', sep='\t',quotechar='"',)
# Regrouper les données par département (depPrD) et calculer le TMJA moyen
depPrD_traffic = data.groupby('depPrD')['TMJA'].mean().reset_index()

# Trier les départements par TMJA décroissant
depPrD_traffic = depPrD_traffic.sort_values(by='TMJA', ascending=False)

# Tracer un graphique en barres
plt.figure(figsize=(12, 6))
sns.barplot(x='depPrD', y='TMJA', data=depPrD_traffic, palette="viridis")

# Ajouter un titre et des labels
plt.title("Départements avec le Trafic Moyen Journalier Annuel (TMJA)", fontsize=14)
plt.xlabel("Département", fontsize=12)
plt.ylabel("TMJA Moyen", fontsize=12)
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
