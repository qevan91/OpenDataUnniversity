import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv('voitures-par-commune-par-energie.csv',on_bad_lines='skip', sep=';', quotechar='"', engine='python')

print(data.dtypes)

data['DATE_ARRETE'] = pd.to_datetime(data['DATE_ARRETE'])

grouped_data = data.groupby('DATE_ARRETE')['NB_VP_RECHARGEABLES_EL'].sum().reset_index()

plt.figure(figsize=(12, 6))
sns.barplot(x='DATE_ARRETE', y='NB_VP_RECHARGEABLES_EL', data=grouped_data)
plt.title('Nombre de Véhicules Rechargeables Électriques par Date')
plt.xlabel('Date')
plt.ylabel('Nombre de Véhicules Rechargeables Électriques')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('parDate.png')
plt.show()