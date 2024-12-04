import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv('donnees_insee_premiere_1978.csv', on_bad_lines='skip', sep=',', quotechar='"', engine='python')

data.columns = data.columns.str.strip()

data['Anne'] = data['Anne'].astype(int)
data['Population au 1er janvier'] = data['Population au 1er janvier'].astype(float)

grouped_data = data.groupby('Anne')['Population au 1er janvier'].sum().reset_index()

plt.figure(figsize=(12, 6))
ax = sns.barplot(x='Anne', y='Population au 1er janvier', data=grouped_data)
ax.set_ylim(60000, 70000)
plt.title('Population au 1er janvier par année')
plt.xlabel('Année')
plt.ylabel('Population au 1er janvier')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('population.png')
plt.show()