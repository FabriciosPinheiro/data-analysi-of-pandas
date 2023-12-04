import pandas as pd
import numpy as np
import datetime

# 1. Carregue os conjuntos de dados "gasolina_2000+.csv" e "gasolina_2010+.csv"
#  em dois DataFrames diferentes e combine-os em um único DataFrame.

data1 = pd.read_csv('gasolina_2000.csv', index_col=0)
data2 = pd.read_csv('gasolina_2010.csv', index_col=0)


df1 = pd.DataFrame(data1)
df2 = pd.DataFrame(data2)

# Retorna os números de Linhas e Colunas
df1.shape
df2.shape

df = pd.concat([df1, df2]) # Cobinado em um único DataFrame
df.shape
df

# 2.Investigue as colunas e entenda o conjunto de dados usando o head() e info()

df.head(10) # Mostra as 5 ou 10 primeiras linhas
df.info()
# O Pandas interpreta object como String

# 3. Selecione a terceira entrada da coluna DATA INICIAL e verifique seu tipo.

df.index # Retorna os índices
type(df['DATA INICIAL'][2]) # Retorna o valor correspondente e seu tipo
type(df.iloc[2, 0]) # Seleciona o elemento da linha 2 e coluna 1 e seu tipo

# 4. Você deve ter percebido que as colunas DATA INICIAL e DATA FINAL estão formatadas como 
# string. Utilizando o método pd.to_datetime(), converta ambas colunas para Timestamp / Datetime.

# Se você estiver trabalhando com um DataFrame do pandas e quiser converter uma 
# coluna de strings em datas, você pode usar a função pd.to_datetime()

# Converte as coluna DATA INICIAL e FINAL para datetime
df['DATA INICIAL'] = pd.to_datetime(df['DATA INICIAL'])
df['DATA FINAL'] = pd.to_datetime(df['DATA FINAL'])
df.info()

type(df['DATA INICIAL'][2])

# 5. Crie uma nova coluna para representar o ano e o mês(aaaa-mm), utilizando a coluna DATA FINAL 
# como referência.

df['ANO MES'] = df['DATA FINAL'] # Cria uma noma Coluna
del df['ANO MES'] # Deleta a Coluna criada
df.drop('ANO MES', axis=1, inplace=True) # Excluiu a coluna criada
df
# Formata a data para o formato 'aaaa-mm': dt.strftime('%Y-%m')
df.insert(loc=2, column='ANO MES', value=df['DATA FINAL'].dt.strftime('%Y-%m')) # Cria uma nova Coluna e insere depois da coluna DATA_FINAL
df.info()

# 6. Utilizando o value_counts(), liste todos os tipos de produtos contidos na base de dados.

df.columns #Lista todas as colunas
df.value_counts() # Mostra os elementos únicos e a quantidade
df['PRODUTO'].value_counts()

# 7. Filtre o DataFrame para obter apenas dados da 'GASOLINA COMUM'. Grave em uma nova variável.

gasolina_comum = df[df['PRODUTO'] == 'GASOLINA COMUM']
gasolina_comum

# A primeira Parte é o Filtro         a segunda é a Seleção
df[df['PRODUTO'] == 'GASOLINA COMUM'][['PRODUTO', 'PREÇO MÉDIO REVENDA', 'ESTADO']].head(10)

# 8. Qual o preço médio de revenda da gasolina em agosto de 2008: 08/2008

gasolina_comum[gasolina_comum['ANO MES'] == '2008-08']['PREÇO MÉDIO REVENDA'].mean()

# 9. Qual o preço médio de revenda da gasolina em maio de 2014 em São Paulo?

gasolina_comum[(gasolina_comum['ANO MES'] == '2014-05') & (gasolina_comum['ESTADO'] == 'SAO PAULO')]['PREÇO MÉDIO REVENDA'].mean()

# 10. Você conseguiria descobrir em qual(quais) estado(s) a gasolina ultrapassou a barreira dos R$ 5,00? 
# E quando isso ocorreu?

gasolina_comum[gasolina_comum['PREÇO MÉDIO REVENDA'] > 5][['ESTADO', 'PREÇO MÉDIO REVENDA', 'ANO MES']].head(10)

# 11. Qual a média de preço dos estados da região sul em 2012?

gasolina_comum.info()
gasolina_comum['ANO MES'] = pd.to_datetime(gasolina_comum['ANO MES'])
gasolina_comum.info()

gasolina_comum['ANO MES'] = gasolina_comum['ANO MES'].dt.year # Retorna apenas o ano
gasolina_comum

gasolina_comum[(gasolina_comum['ANO MES'] == 2012) & (gasolina_comum['REGIÃO'] == 'SUL')]['PREÇO MÉDIO REVENDA'].mean()

# Usando a função lambda
df_aux = gasolina_comum[gasolina_comum['DATA FINAL'].apply(lambda x: x.year) == 2012]
df_aux[df_aux['REGIÃO'] == 'SUL']['PREÇO MÉDIO REVENDA'].mean()

# 12. Você conseguiria obter uma tabela contendo a variação percentual ano a ano para o estado do Rio de Janeiro?

gasolina_comum.insert(loc=2, column='ANO MES', value=df['DATA FINAL'].dt.strftime('%Y/%m'))
gasolina_comum.insert(loc=3, column='MES', value=df['DATA FINAL'].dt.month)
gasolina_comum.info()

df_rio = gasolina_comum[gasolina_comum['ESTADO'] == 'RIO DE JANEIRO']
df_rio

df_mes_rio = df_rio.groupby('ANO MES')[['PREÇO MÉDIO REVENDA', 'MES']].last()
df_mes_rio

(df_mes_rio[df_mes_rio['MES'] == 12] / df_mes_rio[df_mes_rio['MES'] == 12].shift(1) -1) * 100


# DESAFIO: Crie uma tabela contendo uma serie temporal com a diferença absoluta e percentual entre os
#  valores mais baratos e caros. Apresente também ao lado os estados na qual os maiores e menores preços
#  foram registrados.

# Agrupamentos do ANO MES
df_max = gasolina_comum.groupby('ANO MES').max()['PREÇO MÉDIO REVENDA'] # Retorna os Períodos que apresentaram os Maiores valores
df_min = gasolina_comum.groupby('ANO MES').min()['PREÇO MÉDIO REVENDA'] # Os Menores valores

df_diff = pd.DataFrame()

df_diff['abs_diff'] = df_max - df_min # Retorna a Diferença Absoluta
df_diff

df_diff['Va_Perc'] = ((df_max - df_min) / df_min)* 100 # Retorna a variação Percentual
df_diff

# Retorna os índices dos Maiores e Menores valores
idx_max = gasolina_comum.groupby('ANO MES')['PREÇO MÉDIO REVENDA'].idxmax() # Agrupa a Coluna e retorna o Maior valor
idx_min = gasolina_comum.groupby('ANO MES')['PREÇO MÉDIO REVENDA'].idxmin() # Agrupa e retorna o menor valor

idx_max
idx_min

df_diff['max'] = df_max # Cria a coluna max com os maiores valores observados
df_diff['min'] = df_min # Cria a coluna min com os menores valores observados

df_diff # É uma Série Temporal: onde os índices tem como valores data

# Localiza as Lihas por meio dos índices que possuem os Maiores e os menores valores
gasolina_comum.loc[idx_max, :][['ESTADO', 'PREÇO MÉDIO REVENDA', 'ANO MES']] # Retorna o: Estado, Preço M. de Revenda e o ANO
gasolina_comum.loc[idx_min, :][['ESTADO', 'PREÇO MÉDIO REVENDA', 'ANO MES']]

df_diff['ESTADO_MAX'] = gasolina_comum.loc[idx_max, :]['ESTADO'].values
df_diff['ESTADO_MIN'] = gasolina_comum.loc[idx_min, :]['ESTADO'].values

df_diff

df_diff['ESTADO_MAX'].value_counts() # Estados onde a gasolina é mais cara
df_diff['ESTADO_MIN'].value_counts().head() # Estados onde é mais barata