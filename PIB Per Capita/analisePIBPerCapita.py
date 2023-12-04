import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Perguntas - GDP Per Person (1901-2011)

data = pd.read_csv('gdp.csv', decimal='.')
df_gdp = pd.DataFrame(data)

# Limpe o conjunto de dados, convertendo strings em datas ou float, quando necessário.
df_gdp.columns # Retorna os títulos das Colunas
df_gdp['GDP_pp'] = df_gdp[' GDP_pp '] # Criando uma nova coluna
del df_gdp[' GDP_pp ']

type(df_gdp['Country'][0]) # Retorna o tipo de dados da coluna
type(df_gdp['Year'].iloc[0]) #Tipo string
df_gdp['GDP_pp'].iloc[0] # Retorna o dado da coluna


df_gdp.info()
df_gdp['GDP_pp'].value_counts()

#Corta a string retornando uma lsita de String e pega último elemento convertendo para inteiro
df_gdp['Year'] = df_gdp['Year'].apply(lambda x:int(x.split('/')[-1])) # Retorna apenas o último elemento da lista: Ano
df_gdp['Year'].iloc[0] # Mostra o valor do tipo int

df_gdp['GDP_pp'].iloc[0] # Existe espaços na direita e esquerda do valor
df_gdp['GDP_pp'].value_counts() # Os valores das unidades de milhar são compostos por (,) notação dos EUA

df_gdp['GDP'] = df_gdp['GDP_pp'].apply(lambda x: float(x.split()[0].replace(',', '')))
del df_gdp['GDP_pp']

df_gdp['GDP'].value_counts()

# Você conseguiria informar o primeiro valor registrado de cada país?
df_gdp.groupby('Country')['Year'].min()

df_gdp.groupby('Country')['GDP'].mean()

# Informe as regiões com maiores crescimentos de PIB per capita no século passado.
df_gdp_start = df_gdp[df_gdp['Year'] == 1901]
df_gdp_end = df_gdp[df_gdp['Year'] == 1996]

((df_gdp_end.groupby('Region')['GDP'].mean() / df_gdp_start.groupby('Region')['GDP'].mean() -1) * 100).sort_values()

# Preecha os anos ausentes em cada país com uma estimativa, baseada na diferença entre o próximo registro e o anterior.

arr_year = np.arange(df_gdp['Year'].min(), df_gdp['Year'].max())
arr_year

df_all_years = pd.DataFrame(arr_year, columns=['Year'])
df_all_years.index = df_all_years['Year']

df_years_off = ~df_all_years['Year'].isin(df_gdp['Year'])
df_years_off = df_all_years.loc[df_years_off].index

df_gdp = df_gdp.sort_values(['Country', 'Year'])

df_gdp['delta_gdp'] = df_gdp['GDP'] - df_gdp['GDP'].shift(1)
df_gdp['delta_year'] = df_gdp['Year'] - df_gdp['Year'].shift(1)
df_gdp['gdp_year'] = (df_gdp['delta_gdp'] / df_gdp['delta_year']).shift(-1)
df_gdp

df_gdp['next_year'] = df_gdp['Year'].shift(-1)
type(df_gdp['next_year'][0])
del df_gdp['delta_gdp'], df_gdp['delta_year']
df_gdp.head(5)

df_new_data = pd.DataFrame()

for idx, row in df_gdp.iterrows():
    if row['Year'] == 2011:
        continue

    years_to_add = df_years_off[(df_years_off < row['next_year']) & (df_years_off > row['Year'])]

    for new_year in years_to_add:
        add_row = row.copy()
        add_row['GDP'] = (new_year - add_row['Year']) * add_row['gdp_year'] + add_row['GDP']
        add_row['Year'] = new_year
        add_row['kind'] = 'estimated'
        df_new_data = pd.concat([df_new_data, add_row.to_frame().transpose()])

df_new_data

df_gdp = pd.concat([df_gdp, df_new_data])
df_gdp.sort_values(['Country', 'Year'], inplace=True)

df_gdp.index = df_gdp['Year']

df_gdp['kind'].fillna('real', inplace=True)
df_gdp

# Gráfico do PIB per capita do Brasil ao longo dos anos
fig, ax = plt.subplots(figsize=(20, 5))
df_gdp[(df_gdp['kind'] == 'real') & (df_gdp['Country'] == 'Brazil')].plot(kind='scatter', y='GDP', x='Year', ax=ax, title='PIB per capita do Brasil ao longo dos anos', color='green')
df_gdp[(df_gdp['kind'] == 'estimated') & (df_gdp['Country'] == 'Brazil')].plot(kind='scatter', y='GDP', x='Year', ax=ax, color='orange')


# DESAFIOS
# Você conseguiria criar um mapa do gdp ou da obesidade no mundo ao longo dos anos?
# Há uma relação entre níveis de obesidade e gdp per capita?