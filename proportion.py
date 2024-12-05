import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv('Proportion.csv', on_bad_lines='skip', sep=',', quotechar='"', engine='python', header=None, names=['Département', 'Part d\'électrique (%)'])

data.columns = data.columns.str.strip()

data['Part d\'électrique (%)'] = pd.to_numeric(data['Part d\'électrique (%)'], errors='coerce')

data['Département'] = data['Département'].astype(str)

grouped_data = data.groupby('Département')['Part d\'électrique (%)'].sum().reset_index()

plt.figure(figsize=(12, 6))
sns.barplot(x='Département', y='Part d\'électrique (%)', data=grouped_data)
plt.title('Nombre de Véhicules Rechargeables Électriques par Département')
plt.xlabel('Département')
plt.ylabel('Part d\'électrique (%)')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('parDate.png')
plt.show()