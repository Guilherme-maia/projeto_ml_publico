# PROJETO MACHINE LEARNING

As funções implantadas no projeto foram feitas para auxiliar na construção do modelos estatísticos, seja modelos mais simples como uma Regressão Logística ou para algoritmos mais avançados como xgboost ou lightGBM.

A baixo mostro passo a passo quais são as análises mínimas para a construção de um modelo de forma completa.

## Passos a passo

### Identificação do tipo de informação (metadados) 

- Função: 

> ajuste_metadados.py 

Objetivo: Identificar os tipos de variáveis que temos no banco da dados, esse é um passo importante pois as maiorias de algoritmos de ML no python só utilizam dados numericos para a crição do modelo. Caso seja identificado alguma variável categorica teremos que fazer algum tipo de tranformação nessas categorias.

### Descritiva das informações (Estatísticas) <font collor="#ff0000"> EM CONSTRUÇÃO </font>

### Transformações das variáveis (Categoricas) <font collor="#ff0000"> EM CONSTRUÇÃO </font>

- Funções:

> get_woe_categoric.py

> get_dummie.py


### Seleção de variáveis <font collor="#ff0000"> EM CONSTRUÇÃO </font>

- Univariada (Concentração)
- Bivariada (Information Value)
- Multivariada (Recursive Feature Eliminate)

### Ajuste de missing <font collor="#ff0000"> EM CONSTRUÇÃO </font>

- Valor fixo (ex: -999)
- Substituição por meio de estatística (min, media e etc.)

### Amostragem <font collor="#ff0000"> EM CONSTRUÇÃO </font>

- Treino
- Teste/validação
- Out-of-time

### Modelos <font collor="#ff0000"> EM CONSTRUÇÃO </font>

- Logistica Ridge
- Árvore
- Floresta
- ExtraTree
- Xgboost
- Catboost
- LigthGBM

### Comparação de técnicas <font collor="#ff0000"> EM CONSTRUÇÃO </font>

- KS
- ROC

### Filtro por importância (Variáveis) <font collor="#ff0000"> EM CONSTRUÇÃO </font>

- Redução de variáveis 

### Estabilidade no tempo (variáveis finais) <font collor="#ff0000"> EM CONSTRUÇÃO </font>

- Distribuição da variáveis no tempo

### Interpretação de ML <font collor="#ff0000"> EM CONSTRUÇÃO </font>

- Interpretação Simplificada (+/-)
- ShapeValue

### Salvar Modelo Serializado <font collor="#ff0000"> EM CONSTRUÇÃO </font>

- Pickle
