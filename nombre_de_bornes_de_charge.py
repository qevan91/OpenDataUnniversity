import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Charger les données
data = pd.read_csv('consolidation-etalab-schema-irve-statique-v-2.3.1-20241204.csv', on_bad_lines='skip', sep=';', quotechar='"', engine='python')

# Supprimer les duplicatas basés sur la colonne 'adresse_station'
data_unique = data.drop_duplicates(subset='adresse_station')

# Grouper les données par 'adresse_station' et sommer 'nbre_pdc'
grouped_data = data_unique.groupby('adresse_station')['nbre_pdc'].sum().reset_index()

# Créer le graphique
plt.figure(figsize=(12, 6))
sns.lineplot(x='adresse_station', y='nbre_pdc', data=grouped_data)
plt.title("Nombre de bornes de recharges")
plt.xlabel("Lieux")
plt.ylabel("Nombres de bornes")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

