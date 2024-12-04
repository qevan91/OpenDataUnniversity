import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Charger les données
data = pd.read_csv('bornes-irve.csv', on_bad_lines='skip', sep=';', quotechar='"', engine='python')

# Grouper les données par 'adresse_station' et sommer 'nbre_pdc'
grouped_data = data.groupby('Région')['nbre_pdc'].sum().reset_index()

# Créer le graphique
plt.figure(figsize=(12, 6))
sns.barplot(x='Région', y='nbre_pdc', data=grouped_data)
plt.title("Nombre de bornes de recharges")
plt.xlabel("Lieux")
plt.ylabel("Nombres de bornes")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
