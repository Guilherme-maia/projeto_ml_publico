# PROJETO MACHINE LEARNING

As funções implantadas no projeto foram feitas para auxiliar na construção do modelos estatísticos, seja modelos mais simples como uma Regressão Logística ou para algoritmos mais avançados como xgboost ou lightGBM.

A baixo mostro passo a passo quais são as análises mínimas para a construção de um modelo de forma completa.

## Passos a passo

### Identificação do tipo de informação (metadados) 

> ajuste_metadados.py 

Objetivo: Identificar os tipos de variáveis que temos no banco da dados, esse é um passo importante pois as maiorias de algoritmos de ML no python só utilizam dados numericos para a crição do modelo. Caso seja identificado alguma variável categorica teremos que fazer algum tipo de tranformação nessas categorias.

### Descritiva das informações (Estatísticas) <font collor="#ff0000"> EM CONSTRUÇÃO </font>

### Transformações das variáveis (Categoricas) 

> get_woe_categoric.py

> get_dummie.py

### Seleção de variáveis <font collor="#ff0000"> EM CONSTRUÇÃO </font>

> univariada.py: Verifica a concentração máxima em um valor espefícico do banco de dados

> Bivariada (Information Value)

> best_features_fre.py: Visão multivariada (Recursive Feature Eliminate), seleciona "N" variávies mais importantes do seu conjunto de dados

### Ajuste de missing <font collor="#ff0000"> EM CONSTRUÇÃO </font>

> Valor fixo (ex: -999)

> Substituição por meio de estatística (min, media e etc.)

### Amostragem <font collor="#ff0000"> EM CONSTRUÇÃO </font>

> Treino
> Teste/validação
> Out-of-time

### Modelos <font collor="#ff0000"> EM CONSTRUÇÃO </font>

> Logistica Ridge

> Árvore

> Floresta

> ExtraTree

> Xgboost

> Catboost

> LigthGBM

### Alinhamento do Score (Modelo com Segmento)

> alinhamento_de_score.py

Essa função tem como objetivo alinhar as probabilidades dos score quando o modelo tem segmentação. Com essa fórmula garantimos que um indivíduo com um risco "X" que esta na segmento A tenha o mesmo valor de score de um outro indivíduo com o mesmo risco X que esta no segmento B. Em resumo, independente do segmento que os indivíduos se encontram caso eles tenham o mesmo risco (probabidade de default) ele terá a mesma pontuação de score. 

### Comparação de técnicas <font collor="#ff0000"> EM CONSTRUÇÃO </font>

> KS
> ROC

### Filtro por importância (Variáveis) <font collor="#ff0000"> EM CONSTRUÇÃO </font>

> Redução de variáveis 

### Estabilidade no tempo 

> Distribuição das variáveis no tempo

Essa função quebra as variáveis continuas em N categorias, essas mesmas categorias/quebras são aplicadas na base out-of-time (que não foi utilizada no modelo) e assim verificamos de forma gráfica se a distribuição das variáveis mudaram ou não ao longo do tempo.

### Interpretação de ML <font collor="#ff0000"> EM CONSTRUÇÃO </font>

> Interpretação Simplificada (+/-)
> ShapeValue

### Salvar Modelo Serializado <font collor="#ff0000"> EM CONSTRUÇÃO </font>

> Pickle
