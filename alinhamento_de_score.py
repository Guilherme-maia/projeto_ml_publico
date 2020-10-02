def alinhamento_de_score(resposta, prob_0, valor_central = 500, dobra_odds = 100, score_minimo = 1):
    
    """
    ----- Função de alinhamento e padronização do score entre score_minimo e 1000 pontos. -----

    Parâmetros:
        - prob_0: Vetor de resposta do modelo de Machine Learning
        - resposta: Target/Y do banco de dados
        - valor central: Valor central do XBETA
        - dobra odds: Valor que a acada x pontos de XBETA a resposta ira dobrar de quantidade

    """

    from sklearn.linear_model import LogisticRegression
    import warnings
    warnings.simplefilter("ignore")   

    modelo =  LogisticRegression(penalty = 'l2', C = 1,
                                 dual = False, tol = 0.0001, 
                                 fit_intercept = True, 
                                 intercept_scaling = 1, 
                                 max_iter = 1000, 
                                 multi_class = 'ovr').fit(prob_0, resposta)
        
    prob_0['xbeta'] = modelo.intercept_[0] + modelo.coef_[0][0] * prob_0['prob_0']
    prob_0['prescore'] = (valor_central + (prob_0['xbeta']*dobra_odds)/np.log(2))
    prescore_min = prob_0['prescore'].min()
    prescore_max = prob_0['prescore'].max()
    prob_0['SCORE_ALINHADO'] = (score_minimo + 
                    ((prob_0['prescore'] - (prescore_min))*(1000-score_minimo))/(prescore_max - prescore_min)).astype(int)
        
    print("=======================")
    print("Fórmula de Alinhamento")
    print("=======================")
        
    print("")
    print("df['XBETA'] = ", modelo.intercept_[0] ,"+",modelo.coef_[0][0]," * df['prob_0']")
    print("df['PRESCORE'] = (",valor_central,"+ (df['XBETA']*",dobra_odds,")/np.log(2))")
    print("PRESCORE_MIN = ",prescore_min)
    print("PRESCORE_MAX = ",prescore_max)
    print("VALOR_MINIMO = ",score_minimo)
    print("df['SCORE_FINAL'] = (VALOR_MINIMO + ((df['PRESCORE'] - (PRESCORE_MIN))*(1000-VALOR_MINIMO))/(PRESCORE_MAX - PRESCORE_MIN)).astype(int)")   
        
    return pd.concat([prob_0,resposta],axis=1)