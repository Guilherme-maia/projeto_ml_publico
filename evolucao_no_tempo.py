def evolucao_no_tempo(base_ref, base_oot, safra = "safra", quantidade = 10):
    
    from matplotlib import pyplot as plt
    from matplotlib.colors import ListedColormap
    import seaborn as sns
    plt.style.use('ggplot')

    def cut_n(dataframe, quantidade):
        bins = []
        df = dataframe.select_dtypes('number')
        for col in df.columns:
            bins_aux = algos.quantile(df[col], np.linspace(0, 1, quantidade))
            bins.append(bins_aux)
        return pd.DataFrame(bins, index = df.columns).T

    def apply_cut(dataframe, tab_bins):
        df = dataframe.select_dtypes('number')
        dataframe_final = df.drop(df.columns,axis = 1)
        for col in df.columns:
            nome = "fx_"+col
            d1 = pd.DataFrame({nome : pd.cut(df[col], np.unique(tab_bins[col]),include_lowest = True)})
            d1[nome] = d1[nome].astype("category")
            dataframe_final = pd.concat([dataframe_final, d1] , axis = 1)
        return dataframe_final

    tab_bins = cut_n(base_ref.drop([safra],axis=1), 8)
    tabela = pd.concat([base_ref,base_oot],axis = 0, sort = False)
    dados_cat = apply_cut(tabela.drop(safra,axis=1), tab_bins)

    dados_cat = pd.concat([dados_cat,tabela[safra].astype(str)],axis =1)
    dados_cat['value'] = 1
    dados_cat[safra] = dados_cat[safra].astype("category")

    for f in dados_cat.columns.values:
        if ((f != 'value') & (f != safra)):
            nome = f+'.png'
            dados_cat[f] = dados_cat[f].astype("category")
            fig = pd.pivot_table(dados_cat, 
                                index = [safra], 
                                values = ["value"], 
                                columns = [f], 
                                aggfunc = np.sum)\
                    .apply(lambda x: x*100/sum(x), axis = 1)\
                    .plot(kind="bar", 
                          stacked = True, 
                          figsize = (14,6), 
                          colormap = ListedColormap(sns.color_palette("husl", quantidade)))

            plt.legend(loc = 'center left', bbox_to_anchor = (1, .5), ncol = 1,fontsize = 8, title_fontsize = 10)
            plt.title(f,fontdict = {'fontsize' : 12})
            plt.xlabel("Safras", fontsize = 12) 
            plt.ylabel("Percentage (%)", fontsize = 12)
            plt.show();