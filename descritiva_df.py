import pandas as pd
import numpy as np
import os
import subprocess

def descritiva_table(dataframe, metadados):
        
  resumo_num = []
  resumo_cat = []
    
  #Detectando os tipos dos dados
  dados_cat = list(metadados[(metadados.Level  == 'nominal') &
                             (metadados.Role == 'input') & 
                             (metadados.Keep == True)]['Variaveis'])
    
  print("Número de variáveis categóricas: ", len(dados_cat))

  dados_num = list(metadados[((metadados.Level == 'ordinal')|(metadados.Level == 'interval')) & 
                              (metadados.Role == 'input') & (metadados.Keep == True)]['Variaveis'])  

  print("Número de variáveis contínuas: ", len(dados_num))
    
  #Selecionando as variaveis
  tab_categoricas = dataframe[dados_cat]
  tab_numericas = dataframe[dados_num]

  if len(dados_num) > 0:
    resumo_num = pd.DataFrame({'qtd': tab_numericas.shape[0],
                               'qtd_missing': tab_numericas.isnull().sum(),
                               'taxa_missing': tab_numericas.isnull().sum()/tab_numericas.shape[0],
                               'desvio': tab_numericas.std(),
                               'minimo': tab_numericas.min(),
                               'quantil_01': tab_numericas.quantile(q = 0.01).T,
                               'quantil_10': tab_numericas.quantile(q = 0.10).T,
                               'quantil_25': tab_numericas.quantile(q = 0.25).T,
                               'mediana': tab_numericas.median(),
                               'media': tab_numericas.mean(),
                               'quantil_75': tab_numericas.quantile(q = 0.75).T,
                               'quantil_90': tab_numericas.quantile(q = 0.90).T,
                               'quantil_99': tab_numericas.quantile(q = 0.99).T,
                               'maximo': tab_numericas.max()
                                })
            
    resumo_num.to_csv('descritiva_var_numericas.csv')
        
  if len(dados_cat) > 0:
        
    resumo_cat = pd.DataFrame({'qtd': tab_categoricas.shape[0],
                               'qtd_missing': tab_categoricas.isnull().sum(),
                               'taxa_missing': tab_categoricas.isnull().sum()/tab_numericas.shape[0],
                               'cardinalidade': tab_categoricas.nunique()
                              })
        
    resumo_cat.to_csv('descritiva_var_categoricas.csv')
       

  return resumo_num, resumo_cat