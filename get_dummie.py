import pandas as pd
import numpy as np
import os
import subprocess

def get_dummie(dataframe, name_missing = 'missing', cardinality = 15, drop_first = False):
        
    #Pegando somente as categoricas
    dataframe_cat = dataframe[dataframe.select_dtypes('object').columns]
        
    if len(dataframe_cat.columns) == 0:
        return dataframe_cat
                
    #Tratando missing se existir
    dataframe_cat = dataframe_cat.fillna(name_missing)
      
    #Calculando a a cadinalidade das variaveis que sera usado como filtro
    Cardinality = []
    Feature = []
    for f in dataframe_cat.columns:
        Feature.append(f)
        Cardinality.append(dataframe_cat[f].value_counts().shape[0])
    
    #Salvando o resumo pre-filtro
    Resumo = pd.DataFrame()
    Resumo['Variaveis'] = Feature
    Resumo['Cardinality'] = Cardinality
    
    #Filtro com base na cadinalidade
    drop = list(Resumo[(Resumo.Cardinality > cardinality)]['Variaveis'])
    dataframe_cat = dataframe_cat.drop(drop,axis=1)
    list_var_cat = dataframe_cat.columns

    #Funçõe de geração de dummies
    dataframe_cat = pd.get_dummies(dataframe_cat, 
                                   columns = list_var_cat,
                                   drop_first = drop_first, 
                                   prefix = list_var_cat,
                                   prefix_sep = '_')
        
    #Trazendo o index da base de entrada
    final = dataframe_cat.set_index(dataframe.index)
  
    return dataframe_cat
    
  