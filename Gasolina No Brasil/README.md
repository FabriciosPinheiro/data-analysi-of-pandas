## Análise de Dados com Pandas

Link para Dataset: https://www.kaggle.com/datasets/matheusfreitag/gas-prices-in-brazil


```python
import pandas as pd
```

## Neste projeto, trabalharemos com dois arquivos csvs separados, contendo informações sobre o preço da gasolina no Brasil. 

### 1. Carregue os conjuntos de dados "gasolina_2000+.csv" e "gasolina_2010+.csv" em dois DataFrames diferentes e combine-os em um único DataFrame.


```python
data1 = pd.read_csv('gasolina_2000.csv', index_col=0)
data2 = pd.read_csv('gasolina_2010.csv', index_col=0)

df1 = pd.DataFrame(data1)
df2 = pd.DataFrame(data2)


df = pd.concat([df1, df2]) # Cobinado em um único DataFrame
```

```python
df.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>DATA INICIAL</th>
      <th>DATA FINAL</th>
      <th>REGIÃO</th>
      <th>ESTADO</th>
      <th>PRODUTO</th>
      <th>NÚMERO DE POSTOS PESQUISADOS</th>
      <th>UNIDADE DE MEDIDA</th>
      <th>PREÇO MÉDIO REVENDA</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>2004-05-09</td>
      <td>2004-05-15</td>
      <td>CENTRO OESTE</td>
      <td>DISTRITO FEDERAL</td>
      <td>ETANOL HIDRATADO</td>
      <td>127</td>
      <td>R$/l</td>
      <td>1.288</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2004-05-09</td>
      <td>2004-05-15</td>
      <td>CENTRO OESTE</td>
      <td>GOIAS</td>
      <td>ETANOL HIDRATADO</td>
      <td>387</td>
      <td>R$/l</td>
      <td>1.162</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2004-05-09</td>
      <td>2004-05-15</td>
      <td>CENTRO OESTE</td>
      <td>MATO GROSSO</td>
      <td>ETANOL HIDRATADO</td>
      <td>192</td>
      <td>R$/l</td>
      <td>1.389</td>
    </tr>
    <tr>
      <th>3</th>
      <td>2004-05-09</td>
      <td>2004-05-15</td>
      <td>CENTRO OESTE</td>
      <td>MATO GROSSO DO SUL</td>
      <td>ETANOL HIDRATADO</td>
      <td>162</td>
      <td>R$/l</td>
      <td>1.262</td>
    </tr>
    <tr>
      <th>4</th>
      <td>2004-05-09</td>
      <td>2004-05-15</td>
      <td>NORDESTE</td>
      <td>ALAGOAS</td>
      <td>ETANOL HIDRATADO</td>
      <td>103</td>
      <td>R$/l</td>
      <td>1.181</td>
    </tr>
  </tbody>
</table>
</div>



# 2.Investigue as colunas e entenda o conjunto de dados usando o head() e info()


```python
df.head() # Mostra as 5 primeiras linhas
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>DATA INICIAL</th>
      <th>DATA FINAL</th>
      <th>REGIÃO</th>
      <th>ESTADO</th>
      <th>PRODUTO</th>
      <th>NÚMERO DE POSTOS PESQUISADOS</th>
      <th>UNIDADE DE MEDIDA</th>
      <th>PREÇO MÉDIO REVENDA</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>2004-05-09</td>
      <td>2004-05-15</td>
      <td>CENTRO OESTE</td>
      <td>DISTRITO FEDERAL</td>
      <td>ETANOL HIDRATADO</td>
      <td>127</td>
      <td>R$/l</td>
      <td>1.288</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2004-05-09</td>
      <td>2004-05-15</td>
      <td>CENTRO OESTE</td>
      <td>GOIAS</td>
      <td>ETANOL HIDRATADO</td>
      <td>387</td>
      <td>R$/l</td>
      <td>1.162</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2004-05-09</td>
      <td>2004-05-15</td>
      <td>CENTRO OESTE</td>
      <td>MATO GROSSO</td>
      <td>ETANOL HIDRATADO</td>
      <td>192</td>
      <td>R$/l</td>
      <td>1.389</td>
    </tr>
    <tr>
      <th>3</th>
      <td>2004-05-09</td>
      <td>2004-05-15</td>
      <td>CENTRO OESTE</td>
      <td>MATO GROSSO DO SUL</td>
      <td>ETANOL HIDRATADO</td>
      <td>162</td>
      <td>R$/l</td>
      <td>1.262</td>
    </tr>
    <tr>
      <th>4</th>
      <td>2004-05-09</td>
      <td>2004-05-15</td>
      <td>NORDESTE</td>
      <td>ALAGOAS</td>
      <td>ETANOL HIDRATADO</td>
      <td>103</td>
      <td>R$/l</td>
      <td>1.181</td>
    </tr>
  </tbody>
</table>
</div>




```python
df.info() # O Pandas interpreta object como String
```

    <class 'pandas.core.frame.DataFrame'>
    Index: 120823 entries, 0 to 120822
    Data columns (total 18 columns):
     #   Column                         Non-Null Count   Dtype  
    ---  ------                         --------------   -----  
     0   DATA INICIAL                   120823 non-null  object 
     1   DATA FINAL                     120823 non-null  object 
     2   REGIÃO                         120823 non-null  object 
     3   ESTADO                         120823 non-null  object 
     4   PRODUTO                        120823 non-null  object 
     5   NÚMERO DE POSTOS PESQUISADOS   120823 non-null  int64  
     6   UNIDADE DE MEDIDA              120823 non-null  object 
     7   PREÇO MÉDIO REVENDA            120823 non-null  float64
     8   DESVIO PADRÃO REVENDA          120823 non-null  float64
     9   PREÇO MÍNIMO REVENDA           120823 non-null  float64
     10  PREÇO MÁXIMO REVENDA           120823 non-null  float64
     11  MARGEM MÉDIA REVENDA           120823 non-null  object 
     12  COEF DE VARIAÇÃO REVENDA       120823 non-null  float64
     13  PREÇO MÉDIO DISTRIBUIÇÃO       120823 non-null  object 
     14  DESVIO PADRÃO DISTRIBUIÇÃO     120823 non-null  object 
     15  PREÇO MÍNIMO DISTRIBUIÇÃO      120823 non-null  object 
     16  PREÇO MÁXIMO DISTRIBUIÇÃO      120823 non-null  object 
     17  COEF DE VARIAÇÃO DISTRIBUIÇÃO  120823 non-null  object 
    dtypes: float64(5), int64(1), object(12)
    memory usage: 17.5+ MB


# 3. Selecione a terceira entrada da coluna DATA INICIAL e verifique seu tipo.


```python
type(df['DATA INICIAL'][2]) # Retorna o valor correspondente e seu tipo
```




    str



# 4. Você deve ter percebido que as colunas DATA INICIAL e DATA FINAL estão formatadas como string. Utilizando o método pd.to_datetime(), converta ambas colunas para Timestamp / Datetime.


```python
# Converte as coluna DATA INICIAL e FINAL para datetime
df['DATA INICIAL'] = pd.to_datetime(df['DATA INICIAL'])
df['DATA FINAL'] = pd.to_datetime(df['DATA FINAL'])
df.info()
```

    <class 'pandas.core.frame.DataFrame'>
    Index: 120823 entries, 0 to 120822
    Data columns (total 18 columns):
     #   Column                         Non-Null Count   Dtype         
    ---  ------                         --------------   -----         
     0   DATA INICIAL                   120823 non-null  datetime64[ns]
     1   DATA FINAL                     120823 non-null  datetime64[ns]
     2   REGIÃO                         120823 non-null  object        
     3   ESTADO                         120823 non-null  object        
     4   PRODUTO                        120823 non-null  object        
     5   NÚMERO DE POSTOS PESQUISADOS   120823 non-null  int64         
     6   UNIDADE DE MEDIDA              120823 non-null  object        
     7   PREÇO MÉDIO REVENDA            120823 non-null  float64       
     8   DESVIO PADRÃO REVENDA          120823 non-null  float64       
     9   PREÇO MÍNIMO REVENDA           120823 non-null  float64       
     10  PREÇO MÁXIMO REVENDA           120823 non-null  float64       
     11  MARGEM MÉDIA REVENDA           120823 non-null  object        
     12  COEF DE VARIAÇÃO REVENDA       120823 non-null  float64       
     13  PREÇO MÉDIO DISTRIBUIÇÃO       120823 non-null  object        
     14  DESVIO PADRÃO DISTRIBUIÇÃO     120823 non-null  object        
     15  PREÇO MÍNIMO DISTRIBUIÇÃO      120823 non-null  object        
     16  PREÇO MÁXIMO DISTRIBUIÇÃO      120823 non-null  object        
     17  COEF DE VARIAÇÃO DISTRIBUIÇÃO  120823 non-null  object        
    dtypes: datetime64[ns](2), float64(5), int64(1), object(10)
    memory usage: 21.5+ MB


# 5. Crie uma nova coluna para representar o ano e o mês(aaaa-mm), utilizando a coluna DATA FINAL como referência.


```python
# Formata a data para o formato 'aaaa-mm': dt.strftime('%Y-%m')
df.insert(loc=2, column='ANO MES', value=df['DATA FINAL'].dt.strftime('%Y-%m')) # Cria uma nova Coluna e insere depois da coluna DATA_FINAL
```


```python
df.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>DATA INICIAL</th>
      <th>DATA FINAL</th>
      <th>ANO MES</th>
      <th>REGIÃO</th>
      <th>ESTADO</th>
      <th>PRODUTO</th>
      <th>NÚMERO DE POSTOS PESQUISADOS</th>
      <th>UNIDADE DE MEDIDA</th>
      <th>PREÇO MÉDIO REVENDA</th>
  
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>2004-05-09</td>
      <td>2004-05-15</td>
      <td>2004-05</td>
      <td>CENTRO OESTE</td>
      <td>DISTRITO FEDERAL</td>
      <td>ETANOL HIDRATADO</td>
      <td>127</td>
      <td>R$/l</td>
      <td>1.288</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2004-05-09</td>
      <td>2004-05-15</td>
      <td>2004-05</td>
      <td>CENTRO OESTE</td>
      <td>GOIAS</td>
      <td>ETANOL HIDRATADO</td>
      <td>387</td>
      <td>R$/l</td>
      <td>1.162</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2004-05-09</td>
      <td>2004-05-15</td>
      <td>2004-05</td>
      <td>CENTRO OESTE</td>
      <td>MATO GROSSO</td>
      <td>ETANOL HIDRATADO</td>
      <td>192</td>
      <td>R$/l</td>
      <td>1.389</td>
    </tr>
    <tr>
      <th>3</th>
      <td>2004-05-09</td>
      <td>2004-05-15</td>
      <td>2004-05</td>
      <td>CENTRO OESTE</td>
      <td>MATO GROSSO DO SUL</td>
      <td>ETANOL HIDRATADO</td>
      <td>162</td>
      <td>R$/l</td>
      <td>1.262</td>
    </tr>
    <tr>
      <th>4</th>
      <td>2004-05-09</td>
      <td>2004-05-15</td>
      <td>2004-05</td>
      <td>NORDESTE</td>
      <td>ALAGOAS</td>
      <td>ETANOL HIDRATADO</td>
      <td>103</td>
      <td>R$/l</td>
      <td>1.181</td>
    </tr>
  </tbody>
</table>
</div>



# 6. Utilizando o value_counts(), liste todos os tipos de produtos contidos na base de dados.


```python
df['PRODUTO'].value_counts()
```




    PRODUTO
    GASOLINA COMUM        23570
    GLP                   23561
    ETANOL HIDRATADO      23440
    ÓLEO DIESEL           21194
    GNV                   14469
    ÓLEO DIESEL S10        9113
    OLEO DIESEL S10        2376
    OLEO DIESEL            2351
    GASOLINA ADITIVADA      749
    Name: count, dtype: int64



# 7. Filtre o DataFrame para obter apenas dados da 'GASOLINA COMUM'. Grave em uma nova variável.


```python
gasolina_comum = df[df['PRODUTO'] == 'GASOLINA COMUM']
gasolina_comum.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>DATA INICIAL</th>
      <th>DATA FINAL</th>
      <th>ANO MES</th>
      <th>REGIÃO</th>
      <th>ESTADO</th>
      <th>PRODUTO</th>
      <th>NÚMERO DE POSTOS PESQUISADOS</th>
      <th>UNIDADE DE MEDIDA</th>
      <th>PREÇO MÉDIO REVENDA</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>12064</th>
      <td>2004-05-09</td>
      <td>2004-05-15</td>
      <td>2004-05</td>
      <td>CENTRO OESTE</td>
      <td>DISTRITO FEDERAL</td>
      <td>GASOLINA COMUM</td>
      <td>128</td>
      <td>R$/l</td>
      <td>2.029</td>
    </tr>
    <tr>
      <th>12065</th>
      <td>2004-05-09</td>
      <td>2004-05-15</td>
      <td>2004-05</td>
      <td>CENTRO OESTE</td>
      <td>GOIAS</td>
      <td>GASOLINA COMUM</td>
      <td>395</td>
      <td>R$/l</td>
      <td>2.025</td>
    </tr>
    <tr>
      <th>12066</th>
      <td>2004-05-09</td>
      <td>2004-05-15</td>
      <td>2004-05</td>
      <td>CENTRO OESTE</td>
      <td>MATO GROSSO</td>
      <td>GASOLINA COMUM</td>
      <td>194</td>
      <td>R$/l</td>
      <td>2.358</td>
    </tr>
    <tr>
      <th>12067</th>
      <td>2004-05-09</td>
      <td>2004-05-15</td>
      <td>2004-05</td>
      <td>CENTRO OESTE</td>
      <td>MATO GROSSO DO SUL</td>
      <td>GASOLINA COMUM</td>
      <td>166</td>
      <td>R$/l</td>
      <td>2.120</td>
    </tr>
    <tr>
      <th>12068</th>
      <td>2004-05-09</td>
      <td>2004-05-15</td>
      <td>2004-05</td>
      <td>NORDESTE</td>
      <td>ALAGOAS</td>
      <td>GASOLINA COMUM</td>
      <td>106</td>
      <td>R$/l</td>
      <td>2.090</td>
    </tr>
  </tbody>
</table>
</div>



# 8. Qual o preço médio de revenda da gasolina em agosto de 2008: 08/2008


```python
gasolina_comum[gasolina_comum['ANO MES'] == '2008-08']['PREÇO MÉDIO REVENDA'].mean()
```




    2.6012444444444442



# 9. Qual o preço médio de revenda da gasolina em maio de 2014 em São Paulo?


```python
gasolina_comum[(gasolina_comum['ANO MES'] == '2014-05') & (gasolina_comum['ESTADO'] == 'SAO PAULO')]['PREÇO MÉDIO REVENDA'].mean()
```




    2.8822



# 10. Você conseguiria descobrir em qual(quais) estado(s) a gasolina ultrapassou a barreira dos R$ 5,00? E quando isso ocorreu?


```python
gasolina_comum[gasolina_comum['PREÇO MÉDIO REVENDA'] > 5][['ESTADO', 'PREÇO MÉDIO REVENDA', 'ANO MES']].head(10)
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>ESTADO</th>
      <th>PREÇO MÉDIO REVENDA</th>
      <th>ANO MES</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>98201</th>
      <td>ACRE</td>
      <td>5.053</td>
      <td>2018-05</td>
    </tr>
    <tr>
      <th>98347</th>
      <td>ACRE</td>
      <td>5.035</td>
      <td>2018-06</td>
    </tr>
    <tr>
      <th>98493</th>
      <td>ACRE</td>
      <td>5.038</td>
      <td>2018-06</td>
    </tr>
    <tr>
      <th>98511</th>
      <td>RIO DE JANEIRO</td>
      <td>5.016</td>
      <td>2018-06</td>
    </tr>
    <tr>
      <th>98646</th>
      <td>ACRE</td>
      <td>5.031</td>
      <td>2018-06</td>
    </tr>
    <tr>
      <th>98797</th>
      <td>ACRE</td>
      <td>5.036</td>
      <td>2018-06</td>
    </tr>
    <tr>
      <th>98948</th>
      <td>ACRE</td>
      <td>5.039</td>
      <td>2018-06</td>
    </tr>
    <tr>
      <th>99098</th>
      <td>ACRE</td>
      <td>5.021</td>
      <td>2018-07</td>
    </tr>
    <tr>
      <th>99247</th>
      <td>ACRE</td>
      <td>5.042</td>
      <td>2018-07</td>
    </tr>
    <tr>
      <th>99398</th>
      <td>ACRE</td>
      <td>5.038</td>
      <td>2018-07</td>
    </tr>
  </tbody>
</table>
</div>



# 11. Qual a média de preço dos estados da região sul em 2012?


```python
# Usando a função lambda
df_aux = gasolina_comum[gasolina_comum['DATA FINAL'].apply(lambda x: x.year) == 2012]
df_aux[df_aux['REGIÃO'] == 'SUL']['PREÇO MÉDIO REVENDA'].mean()
```




    2.7214423076923073

# DESAFIO: Crie uma tabela contendo uma serie temporal com a diferença absoluta e percentual entre os valores mais baratos e caros. Apresente também ao lado os estados na qual os maiores e menores preços foram registrados.


```python
# Agrupamentos do ANO MES
df_max = gasolina_comum.groupby('ANO MES').max()['PREÇO MÉDIO REVENDA'] # Retorna os Períodos que apresentaram os Maiores valores
df_min = gasolina_comum.groupby('ANO MES').min()['PREÇO MÉDIO REVENDA'] # Os Menores valores
```


```python
df_diff = pd.DataFrame()
df_diff['abs_diff'] = df_max - df_min # Retorna a Diferença Absoluta
df_diff['va_perc'] = ((df_max - df_min) / df_min)* 100 # Retorna a variação Percentual

# Retorna os índices dos Maiores e Menores valores
idx_max = gasolina_comum.groupby('ANO MES')['PREÇO MÉDIO REVENDA'].idxmax() # Agrupa a Coluna e retorna o Maior valor
idx_min = gasolina_comum.groupby('ANO MES')['PREÇO MÉDIO REVENDA'].idxmin() # Agrupa e retorna o menor valor


df_diff['max'] = df_max # Cria a coluna max com os maiores valores observados
df_diff['min'] = df_min # Cria a coluna min com os menores valores observados

df_diff # É uma Série Temporal: onde os índices tem como valores data (Tempo)
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>abs_diff</th>
      <th>va_perc</th>
      <th>max</th>
      <th>min</th>
    </tr>
    <tr>
      <th>ANO MES</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2004-05</th>
      <td>0.550</td>
      <td>29.131356</td>
      <td>2.438</td>
      <td>1.888</td>
    </tr>
    <tr>
      <th>2004-06</th>
      <td>0.584</td>
      <td>30.543933</td>
      <td>2.496</td>
      <td>1.912</td>
    </tr>
    <tr>
      <th>2004-07</th>
      <td>0.609</td>
      <td>31.456612</td>
      <td>2.545</td>
      <td>1.936</td>
    </tr>
    <tr>
      <th>2004-08</th>
      <td>0.530</td>
      <td>26.108374</td>
      <td>2.560</td>
      <td>2.030</td>
    </tr>
    <tr>
      <th>2004-09</th>
      <td>0.539</td>
      <td>26.538651</td>
      <td>2.570</td>
      <td>2.031</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>2021-01</th>
      <td>1.383</td>
      <td>36.109661</td>
      <td>5.213</td>
      <td>3.830</td>
    </tr>
    <tr>
      <th>2021-02</th>
      <td>1.688</td>
      <td>40.960932</td>
      <td>5.809</td>
      <td>4.121</td>
    </tr>
    <tr>
      <th>2021-03</th>
      <td>2.109</td>
      <td>46.058091</td>
      <td>6.688</td>
      <td>4.579</td>
    </tr>
    <tr>
      <th>2021-04</th>
      <td>1.450</td>
      <td>30.353779</td>
      <td>6.227</td>
      <td>4.777</td>
    </tr>
    <tr>
      <th>2021-05</th>
      <td>1.391</td>
      <td>28.580234</td>
      <td>6.258</td>
      <td>4.867</td>
    </tr>
  </tbody>
</table>
<p>204 rows × 4 columns</p>
</div>




```python
# Localiza as Lihas por meio dos índices que possuem os Maiores e os menores valores
gasolina_comum.loc[idx_max, :][['ESTADO', 'PREÇO MÉDIO REVENDA', 'ANO MES']] # Retorna o: Estado, Preço M. de Revenda e o ANO
gasolina_comum.loc[idx_min, :][['ESTADO', 'PREÇO MÉDIO REVENDA', 'ANO MES']]

df_diff['ESTADO_MAX'] = gasolina_comum.loc[idx_max, :]['ESTADO'].values
df_diff['ESTADO_MIN'] = gasolina_comum.loc[idx_min, :]['ESTADO'].values

df_diff # Retorna um DataFrame os seguintes valores abixos
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>abs_diff</th>
      <th>va_perc</th>
      <th>max</th>
      <th>min</th>
      <th>ESTADO_MAX</th>
      <th>ESTADO_MIN</th>
    </tr>
    <tr>
      <th>ANO MES</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2004-05</th>
      <td>0.550</td>
      <td>29.131356</td>
      <td>2.438</td>
      <td>1.888</td>
      <td>ACRE</td>
      <td>SAO PAULO</td>
    </tr>
    <tr>
      <th>2004-06</th>
      <td>0.584</td>
      <td>30.543933</td>
      <td>2.496</td>
      <td>1.912</td>
      <td>MATO GROSSO</td>
      <td>SAO PAULO</td>
    </tr>
    <tr>
      <th>2004-07</th>
      <td>0.609</td>
      <td>31.456612</td>
      <td>2.545</td>
      <td>1.936</td>
      <td>ACRE</td>
      <td>DISTRITO FEDERAL</td>
    </tr>
    <tr>
      <th>2004-08</th>
      <td>0.530</td>
      <td>26.108374</td>
      <td>2.560</td>
      <td>2.030</td>
      <td>MATO GROSSO</td>
      <td>SAO PAULO</td>
    </tr>
    <tr>
      <th>2004-09</th>
      <td>0.539</td>
      <td>26.538651</td>
      <td>2.570</td>
      <td>2.031</td>
      <td>ACRE</td>
      <td>SAO PAULO</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>2021-01</th>
      <td>1.383</td>
      <td>36.109661</td>
      <td>5.213</td>
      <td>3.830</td>
      <td>ACRE</td>
      <td>AMAPA</td>
    </tr>
    <tr>
      <th>2021-02</th>
      <td>1.688</td>
      <td>40.960932</td>
      <td>5.809</td>
      <td>4.121</td>
      <td>ACRE</td>
      <td>AMAPA</td>
    </tr>
    <tr>
      <th>2021-03</th>
      <td>2.109</td>
      <td>46.058091</td>
      <td>6.688</td>
      <td>4.579</td>
      <td>ACRE</td>
      <td>AMAPA</td>
    </tr>
    <tr>
      <th>2021-04</th>
      <td>1.450</td>
      <td>30.353779</td>
      <td>6.227</td>
      <td>4.777</td>
      <td>ACRE</td>
      <td>AMAPA</td>
    </tr>
    <tr>
      <th>2021-05</th>
      <td>1.391</td>
      <td>28.580234</td>
      <td>6.258</td>
      <td>4.867</td>
      <td>ACRE</td>
      <td>AMAPA</td>
    </tr>
  </tbody>
</table>
<p>204 rows × 6 columns</p>
</div>




```python
df_diff['ESTADO_MAX'].value_counts() # Estados onde a gasolina é mais cara
```
    ESTADO_MAX
    ACRE              166
    MATO GROSSO        25
    RIO DE JANEIRO     11
    RORAIMA             2
    Name: count, dtype: int64

```python
df_diff['ESTADO_MIN'].value_counts().head() # Estados onde a gasolina é mais barata
```
    ESTADO_MIN
    SAO PAULO    40
    AMAPA        38
    PIAUI        28
    PARAIBA      28
    PARANA       14
    Name: count, dtype: int64

