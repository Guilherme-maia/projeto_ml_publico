def ks_roc_gini_safra(dataframe,conceito,score,safra,plot=False):
    
    filtros_safra = dataframe[safra].unique()
    filtros_safra.sort()
    ks_calculados = []
    roc_calculados = []
    gini_calculados = []
    qtd_calculado = []
    taxa_target = []
        
    for i in filtros_safra:
   
        #Filtrando a base com a safra de referência
        df_new = dataframe.loc[(dataframe[safra] == i)].copy()
                
        #Calculo de KS
        n_good = df_new[(df_new[conceito] == 0)]
        n_bad  = df_new[(df_new[conceito] == 1)]
        ks = stats.ks_2samp(n_good[score],n_bad[score])[0]*100
    
        #Cálculo de Roc e Gini
        fpr, tpr, threshold = metrics.roc_curve(df_new[conceito], df_new[score])
        roc = 100*auc(fpr, tpr)
        gini = 100*(2*roc/100 - 1)
    
        taxa_target.append(100*(df_new[(df_new[conceito] == 1)].shape[0]/df_new.shape[0]))
        qtd_calculado.append(df_new.shape[0])
        ks_calculados.append(ks)
        roc_calculados.append(roc)
        gini_calculados.append(gini)
    
    estatisticas = pd.DataFrame({'Safra': filtros_safra,
                                 #'Safra': (str(w) for w in filtros_safra),
                                 'Qtd': qtd_calculado, 
                                 'Taxa_1': taxa_target,
                                 'Ks': ks_calculados,
                                 'Roc': roc_calculados,
                                 'Gini': gini_calculados})
   
    if plot == True:
        plt.style.use('seaborn-darkgrid')
        plt.figure(figsize = (7,4))
        lw = 2
        plt.plot(estatisticas['Safra'], estatisticas['Ks'], lw = lw, color = 'blue')
        plt.ylim([0, 100])
        plt.xlabel('Safras', fontsize = 15)
        plt.ylabel('KS', fontsize = 15)
        plt.title('Acompanhamento - KS', fontsize = 18)
        plt.show()
    
        plt.style.use('seaborn-darkgrid')
        plt.figure(figsize = (7,4))
        lw = 2
        plt.plot(estatisticas['Safra'], estatisticas['Roc'], lw=lw, color='blue')
        plt.ylim([40, 100])
        plt.xlabel('Safras', fontsize=15)
        plt.ylabel('Roc', fontsize=15)
        plt.title('Acompanhamento - Roc', fontsize = 18)
        plt.show()
        
        plt.style.use('seaborn-darkgrid')
        plt.figure(figsize = (7,4))
        lw = 2
        plt.plot(estatisticas['Safra'], estatisticas['Gini'], lw=lw, color='blue')
        plt.ylim([0, 100])
        plt.xlabel('Safras', fontsize=15)
        plt.ylabel('Gini', fontsize=15)
        plt.title('Acompanhamento - Gini', fontsize = 18)
        plt.show()
        
    return estatisticas