import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv('voitures-par-commune-par-energie.csv')

data['DATE_ARRETE'] = pd.to_datetime(data['DATE_ARRETE'])

grouped_data = data.groupby(['LIBEPCI', 'DATE_ARRETE'])['NB_VP_RECHARGEABLES_EL'].sum().reset_index()

plt.figure(figsize=(12, 6))

sns.lineplot(data=grouped_data, x='DATE_ARRETE', y='NB_VP_RECHARGEABLES_EL', hue='LIBEPCI', marker="o")
plt.title('Nombre de Véhicules Rechargeables Électriques par EPCI au fil du temps')
plt.xlabel('Date')
plt.ylabel('Nombre de Véhicules Rechargeables Électriques')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
