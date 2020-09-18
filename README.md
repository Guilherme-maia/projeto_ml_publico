# PROJETO MACHINE LEARNING

As funções implantadas no projeto foram feitas para auxiliar na construção do modelos estatísticos, seja modelos mais simples como uma Regressão Logística ou para algoritmos mais avançados como xgboost ou lightGBM.

A baixo mostro passo a passo das mínimas análises que entendo que são necessárias para a construção de um modelo completo.

## Passos a passo

### Identificação do tipo de informação (metadados)

- Numericos: 
- Categoricos:

### Descritiva das informações (Estatísticas) <font COLOR="#ff0000"> EM CONSTRUÇÃO </font>

### Transformações das variáveis (Categoricas)

- WOE
- Dummies

### Seleção de variáveis

- Univariada (Concentração)
- Bivariada (Information Value)
- Multivariada (Recursive Feature Eliminate)

### Ajuste de missing

- Valor fixo (ex: -999)
- Substituição por meio de estatística (min, media e etc.)

### Amostragem

- Treino
- Teste/validação
- Out-of-time

### Modelos

- Logistica Ridge
- Árvore
- Floresta
- ExtraTree
- Xgboost
- Catboost
- LigthGBM

### Comparação de técnicas

- KS
- ROC

### Filtro por importância (Variáveis)

- Redução de variáveis 

### Estabilidade no tempo (variáveis finais)

- Distribuição da variáveis no tempo

### Interpretação de ML

- Interpretação Simplificada (+/-)
- ShapeValue

### Salvar Modelo Serializado

- Pickle
