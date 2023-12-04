import pandas as pd
import numpy as np

#Perguntas - Obesity among adults by country, 1975-2016

df_data = pd.read_csv('obesity_cleaned.csv', index_col=0)

df_obesity = pd.DataFrame(df_data)
df_obesity

# Limpe os dados do DataFrame, criando uma coluna de nome 'Obesity' que conterá os valores de obesidade.
# Transforme em float as colunas que porventura foram importadas como string.
df_obesity.info()

df_obesity['Obesity (%)'].value_counts() # Existem valores de obsidade não coletado de países (No data = 504)
df_obesity.columns # Mostra as colunas do DaraFrame

type(df_obesity['Sex'][0]) # Saber o tipo de dados de cada Coluna

#Cria uma nova coluna copiando os dados da Obesity (%) e Corta os valores de porcentagem de obsidade 
# pelo índixe 0 da String

df_obesity['Obesity'] = df_obesity['Obesity (%)'].str.split().str[0] # Armazena o primeiro valor da String

df_obesity['Obesity'] = pd.to_numeric(df_obesity['Obesity'], errors='coerce') # Converte os valores de String para Float
type(df_obesity['Obesity'][0])

df_obesity['Obesity'].value_counts()

df_obesity.loc[df_obesity['Obesity'] == 'No', 'Obesity'] = np.nan # Passa o índice e a coluna para alteração
df_obesity['Obesity'] = df_obesity['Obesity'].dropna() # Apaga os valores NaN

df_obesity.set_index('Year', inplace=True) # Define a Coluna Year como índice, agora temos uma Série Temporal

del df_obesity['Obesity (%)'] # Apaga a coluna
df_obesity.info()

# Qual o percentual médio de obesidade por sexo no mundo no ano de 2015?

# Agrupa os sexo e retorna às médias
df_obesity[df_obesity.index == 2015].groupby('Sex').mean('Obesity') # Retorna um DataFrame passando index por Year ser o índice

# Quais são os 5 países com a maior e a menor taxa de aumento nos índices de obesidade no período observado?

df_obesity_start = df_obesity[df_obesity.index == 1975] # Define o ínicio do período
df_obesity_end = df_obesity[df_obesity.index == 2016] # Fim do período

df_obesity_start.set_index('Country', inplace=True) # Define o País como índice
df_obesity_end.set_index('Country', inplace=True)

# Evolução da Obesidade
df_obesity_evo = df_obesity_end[df_obesity_end['Sex'] == 'Both sexes']['Obesity'] - df_obesity_start[df_obesity_start['Sex'] == 'Both sexes']['Obesity']
df_obesity_evo

df_obesity_evo.sort_values() # Retorna alguns países que não possui os valores de Obesidade
df_obesity_evo.sort_values().dropna().head(5) #Ordena os valores, descarta os que não possuem os valores de obesidade e retorna os 5 primeiros que os menores índices de Obesidade
df_obesity_evo.sort_values().dropna().tail(5) #Maiores índices de Obesidade

# Quais os países com maiores e menores níveis percetuais de obesidade em 2015?

df_2015 = df_obesity[df_obesity.index == 2015] # Retorna os valores de obesidade de 2015
df_2015[df_2015['Obesity'] == df_2015['Obesity'].max()] # Retorna com o Maior índice de obesidade 
df_2015[df_2015['Obesity'] == df_2015['Obesity'].min()] # O menor índice

# Qual a diferença média percentual de obesidade entre sexos ao longo dos anos para o Brasil?

df_brasil = df_obesity[df_obesity['Country'] == 'Brazil']

# Diferença entre os sexos no Brasil
(df_brasil[df_brasil['Sex'] == 'Female']['Obesity'] - df_brasil[df_brasil['Sex'] == 'Male']['Obesity']).plot() # Mostra que as mulheres ao longo dos anos se tornaram mais obesas do que os homens

# Você conseguiria plotar um gráfico mostrando a evolução da obesidade para ambos sexos no mundo?

df_both = df_obesity[df_obesity['Sex'] == 'Both sexes']
(df_both.groupby('Year')['Obesity'].mean()).plot() # Crescimento da obesidade Mundial para ambos os sexos é crescente


