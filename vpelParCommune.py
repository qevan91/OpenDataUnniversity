import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv('voitures-par-commune-par-energie.csv', on_bad_lines='skip', sep=';', quotechar='"', engine='python')

data['DATE_ARRETE'] = pd.to_datetime(data['DATE_ARRETE'])

grouped_data = data.groupby('LIBEPCI')['NB_VP_RECHARGEABLES_EL'].sum().reset_index()

top_10_epci = grouped_data.nlargest(10, 'NB_VP_RECHARGEABLES_EL')

plt.figure(figsize=(12, 6))
sns.barplot(data=top_10_epci, x='LIBEPCI', y='NB_VP_RECHARGEABLES_EL', palette='viridis')
plt.title('Top 10 des EPCI avec le plus de Véhicules Rechargeables Électriques')
plt.xlabel('EPCI')
plt.ylabel('Nombre de Véhicules Électriques')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('Top10Vehicules.png')
plt.show()