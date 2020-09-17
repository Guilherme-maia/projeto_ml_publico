def ajuste_metadados(dataframe): 
    
    '''
    Função que identifica os tipos das variáveis presentes em um banco de dados

    Entrada: DataFrame qualquer
    Saida: Tabela com as seguintes informações:
        - Variáveis
        - Role: Target, Id ou Imput
        - Level: Binario, Nominal, Intervalar ou Ordinal
        - Keep: 
        - Tipo: 
        - Cardinalidade
        - Quantidade de Missing

    '''

    # Verifica os tipos de variáveis presentes na tabela de treino
    t = []
    for i in dataframe.columns:
        t.append(dataframe[i].dtype)

    n = []
    for i in dataframe.columns:
        n.append(i)

    aux_t = pd.DataFrame(data = t, columns=["Tipos"])
    aux_n = pd.DataFrame(data = n, columns=["Variaveis"])
    df_tipovars = pd.concat([aux_t, aux_n.reindex(columns=aux_t.columns)])

    data = []
    for f in dataframe.columns:

        # Definindo o papel das variáveis:
        if f == 'target':
            role = 'target'
        elif f == 'id':
            role = 'id'
        else:
            role = 'input'

        # Definindo o tipo das variáveis: nominal, ordinal, binary ou interval
        if f == 'target':
            level = 'binary'
        if dataframe[f].dtype == 'object' or f == 'id': 
            level = 'nominal'
        elif dataframe[f].dtype in ['float','float64','float32'] :
            level = 'interval'
        elif dataframe[f].dtype in ['int','int64','int32'] :
            level = 'ordinal'

        # Todas variáveis são incializadas com keep exceto o id e safra
        keep = True
        if f == 'id':
            keep = False
        if f == 'safra':
            keep = False

        # Definindo o tipo das variáveis da tabela de entrada
        dtype = dataframe[f].dtype

        # Criando a lista com todo metadados
         f_dict = {'Variaveis': f, 
                   'Role': role,
                   'Level': level,
                   'Keep': keep,
                   'Tipo': dtype}
         
        data.append(f_dict)
    
    meta = pd.DataFrame(data, columns = ['Variaveis', 'Role', 'Level', 'Keep', 'Tipo'])

    # Quantidade de domínios distintos para cada cariável do tipo ordinal e nominal
    card = []

    v = dataframe.columns
    for f in v:
        dist_values = dataframe[f].value_counts().shape[0]
        qtd_missing = dataframe[f].isnull().sum()
         f_dict = {'Variaveis': f,
                   'Cardinality': dist_values,
                   'Qtd_Missing': qtd_missing
                 }
        card.append(f_dict)

    card = pd.DataFrame(card, columns=['Variaveis', 'Cardinality','Qtd_Missing'])
    
    metadados_train = pd.merge(meta, card, on='Variaveis')

    return metadados_train