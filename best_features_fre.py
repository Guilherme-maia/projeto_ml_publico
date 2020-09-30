def best_features_fre(x_train, y_train, qtd_var = 20, valor_se_missing = -999, tipo_de_modelo = 'LogisticRegression'):
    
    from sklearn.feature_selection import RFE
    from sklearn.linear_model import LinearRegression
    from sklearn.ensemble import RandomForestClassifier
    from sklearn.ensemble import ExtraTreesClassifier
    
    print("Você escolheu a técnica: ", tipo_de_modelo)
    resumo = pd.DataFrame()
            
    x_train[np.isnan(x_train)] = valor_se_missing    

    if tipo_de_modelo == 'LogisticRegression':
        model = LogisticRegression()
        rfe = RFE(model, qtd_var)
        fit = rfe.fit(x_train, y_train)
        resumo['Variaveis'] = list(x_train.columns)
        resumo['fl_elegivel_RFE'] = np.where(rfe.support_ == False, 0, 1)
    
    elif tipo_de_modelo == 'RandomForestClassifier':
        model = RandomForestClassifier()
        rfe = RFE(model, qtd_var)
        fit = rfe.fit(x_train, y_train)
        resumo['Variaveis'] = list(x_train.columns)
        resumo['fl_elegivel_RFE'] = np.where(rfe.support_ == False, 0, 1)
            
    elif tipo_de_modelo == 'ExtraTreesClassifier':
        model = ExtraTreesClassifier()
        rfe = RFE(model, qtd_var)
        fit = rfe.fit(x_train, y_train)
        resumo['Variaveis'] = list(x_train.columns)
        resumo['fl_elegivel_RFE'] = np.where(rfe.support_ == False, 0, 1)
            
    else:
        print("""
        ***************************************
        tipo_de_modelo não suportado, tente:
            -LogisticRegression
            -RandomForestClassifier
            -ExtraTreesClassifier
        ***************************************
        """)
        return False
    
    return resumo