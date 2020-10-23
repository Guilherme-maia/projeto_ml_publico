import pandas as pd
import numpy as np
import os
import subprocess

def get_woe_categoric(dataframe, target = 'target', name_missing = "missing"):

    bons = dataframe[target] == 0
    maus = dataframe[target] == 1

    #Pegando somente as categoricas
    dataframe_cat = dataframe[dataframe.select_dtypes('object').columns]
    dataframe_cat = dataframe_cat.fillna(name_missing)
    transform_vars_list = dataframe_cat.columns

    df_final = dataframe_cat.drop(dataframe_cat.columns,axis = 1)

    WOE = pd.DataFrame(columns = {'Value_Max','Bons', 'Maus', 'Variavel','ODDS','PD','WoE','IV Parcial'})

    for f in dataframe_cat.columns:

    ##########################################
    ######### CALCULANDO O WOE ###############
    ##########################################

        # Contagem de bons e maus por categoria
        tab_bons = pd.crosstab(dataframe_cat[f], columns='#', aggfunc='sum', dropna=False, values=bons)
        tab_maus = pd.crosstab(dataframe_cat[f], columns='#', aggfunc='sum', dropna=False, values=maus)

        # Montagem das variáveis
        tabela_final = pd.DataFrame({'Bons':tab_bons['#']/tab_bons['#'].sum(),
                                     'Maus':tab_maus['#']/tab_maus['#'].sum()})

        #Truncamento   
        tabela_final['Variavel'] = f
        tabela_final['Bons'] = tabela_final['Bons'].replace(0, 0.0001)
        tabela_final['Maus'] = tabela_final['Maus'].replace(0, 0.0001)
        tabela_final['ODDS'] = (tab_bons['#']/tab_bons['#'].sum())/(tab_maus['#']/tab_maus['#'].sum())
        tabela_final['PD'] = tab_maus['#'] / (tab_bons['#'] + tab_maus['#'])
        tabela_final['WoE'] = np.log(tabela_final['Bons']/tabela_final['Maus'])
        tabela_final['IV Parcial'] = (tabela_final['Bons'] - tabela_final['Maus'])*tabela_final['WoE'] 
        tabela_final.reset_index(inplace = True) 
        tabela_final.rename(columns = {f: 'Value_Max'}, inplace = True)

        WOE = pd.concat([WOE,tabela_final],axis = 0)

    ###########################################################
    ######### SUBSTITUINDO O WOE NAS CATEGORIAS ###############
    ###########################################################

    for f in dataframe_cat.columns:
        small_df = WOE[WOE['Variavel'] == f]
        transform_dict = dict(zip(small_df.Value_Max,small_df.WoE))
        replace_cmd = ''
        replace_cmd1 = ''
        for i in sorted(transform_dict.items()):
            replace_cmd = replace_cmd + str(i[1]) + str(' if x <= ') + str(i[0]) + ' else '
            replace_cmd1 = replace_cmd1 + str(i[1]) + str(' if x == "') + str(i[0]) + '" else '
        replace_cmd = replace_cmd + '0'
        replace_cmd1 = replace_cmd1 + '0'
        if replace_cmd != '0':
            try:
                df_final['woe_' + f] = dataframe_cat[f].apply(lambda x: eval(replace_cmd))
            except:
                df_final['woe_' + f] = dataframe_cat[f].apply(lambda x: eval(replace_cmd1))

    return df_final,WOE