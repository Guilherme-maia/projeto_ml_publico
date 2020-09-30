def ks_roc_gini(dataframe,conceito,score,plot = True, dimensao = [5,4]):

    n_good = dataframe[dataframe[conceito] == 0]
    n_bad  = dataframe[dataframe[conceito] == 1]

    # Cálculo de KS
    ks = stats.ks_2samp(n_good[score],n_bad[score])[0]*100
    
    # Cálculo de Roc e Gini
    fpr, tpr, threshold = metrics.roc_curve(dataframe[conceito], dataframe[score])
    roc = 100*auc(fpr, tpr)
    gini = 100*(2*roc/100 - 1)
    
    estatisticas = {'ks': ks,'roc': roc,'gini': gini}

    if plot == True:
        plt.style.use('seaborn-darkgrid')
        plt.figure(figsize=(dimensao[0],dimensao[1]))
        lw = 2
        plt.plot(fpr, tpr, color='blue',lw=lw, label='Roc (%0.0f)' % roc)
        plt.plot(fpr, tpr, color='blue',lw=lw, label='Gini (%0.0f)' % gini)
        plt.plot(fpr, tpr, color='blue',lw=lw, label='Ks (%0.0f)' % ks)
        plt.plot([0, 1], [0, 1], color='navy', lw=lw, linestyle='--')
        plt.xlim([0.0, 1.0])
        plt.ylim([0.0, 1.05])
        plt.xlabel('Falso Positivo', fontsize=12)
        plt.ylabel('Verdadeiro Positivo', fontsize=12)
        plt.legend(loc="lower right")
        plt.legend(fontsize=12) 
        plt.title('Curva ROC', fontsize=12)
        plt.show()
 
    return estatisticas