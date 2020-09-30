def univariada(nome_modelo = "modelo_teste", metadados, base, perc_corte = 0.98):
   
    n = base.shape[0]
    vet_max_variabilidade = []
    vet_nomes = []
    vet_fl_variabilidade = []
    n_vars = base.shape[1]

    for i in range(0,n_vars):
        clear_output(wait = True)
        display(progresso_barra(value = i , value_min = 1, value_max = n_vars - 1, step = 1))
        
        nome_variavel  = base.columns[i]
        a = base.groupby(nome_variavel)[nome_variavel].count()
        a = a/n
        vet_nomes.append(nome_variavel)
        vet_max_variabilidade.append(np.max(a))

    df_concentracao = pd.DataFrame({'Variaveis': vet_nomes,'varibilidade_uni': vet_max_variabilidade})
    df_concentracao['fl_elegivel_uni'] = np.where(df_concentracao.varibilidade_uni > perc_corte, 0, 1)
    df_concentracao.to_csv("log_univariada_"+str(nome_modelo)+".txt", sep = ';', index = False)
    
    return df_concentracao.sort_values(['varibilidade_uni'],ascending=0)