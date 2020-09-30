def ks_roc_gini_train_test(dataframe1,dataframe2,conceito,score, plot = True ,dimensao=[5,4]):
     
    n_good_train = dataframe1[dataframe1[conceito] == 0]
    n_bad_train = dataframe1[dataframe1[conceito] == 1]
    
    n_good_teste = dataframe2[dataframe2[conceito] == 0]
    n_bad_teste  = dataframe2[dataframe2[conceito] == 1]

    # Cálculo de KS
    ks_treino = stats.ks_2samp(n_good_train[score],n_bad_train[score])[0]*100
    ks_teste = stats.ks_2samp(n_good_teste[score],n_bad_teste[score])[0]*100
    
    #Cálculo de Roc
    fpr_treino, tpr_treino, threshold = metrics.roc_curve(dataframe1[conceito], dataframe1[score])
    fpr_teste, tpr_teste, threshold = metrics.roc_curve(dataframe2[conceito], dataframe2[score])
    
    roc_treino = 100*auc(fpr_treino, tpr_treino)
    gini_treino = 100*(2*roc_treino/100 - 1)
    
    roc_teste = 100*auc(fpr_teste, tpr_teste)
    gini_test = 100*(2*roc_teste/100 - 1)
  
    estatisticas = {'ks_treino': ks_treino,
                    'ks_teste': ks_teste,
                    'roc_treino': roc_treino,
                    'roc_teste': roc_teste,
                    'gini_treino': gini_treino,
                    'gini_teste': gini_test}
    
    if plot == True:
        plt.style.use('seaborn-darkgrid')
        plt.figure(figsize=(dimensao[0],dimensao[1]))

        plt.plot(fpr_treino, tpr_treino, color='blue',lw=2, label='Roc (Treino = %0.0f)' % roc_treino)
        plt.plot(fpr_teste, tpr_teste, color='darkorange',lw=2, label='Roc (Teste = %0.0f)' % roc_teste)

        plt.plot([0, 1], [0, 1], color='navy', lw=2, linestyle='--')
        plt.xlim([0.0, 1.0])
        plt.ylim([0.0, 1.05])
        plt.xlabel('Falso Positivo', fontsize=12)
        plt.ylabel('Verdadeiro Positivo', fontsize=12)
        plt.legend(loc="lower right")
        plt.legend(fontsize=12) 
        plt.title('Curva ROC', fontsize=12)
        plt.show()
   
    return estatisticas