# Detecção de Anomalias em Transações Financeiras com Python

## 📌 Sobre o Projeto
Este projeto foi desenvolvido como parte do meu Desafio de Projeto da DIO. O objetivo foi criar um sistema automatizado capaz de identificar transações financeiras suspeitas em um conjunto de dados, utilizando critérios de limite de valor e análise de horário.

## 🚀 Tecnologias Utilizadas
* **Python 3.x**
* **Pandas**: Para manipulação e limpeza de dados.
* **Matplotlib**: Para geração de gráficos e visualização de anomalias.

## 📊 Como Funciona
O script analisa um DataFrame contendo IDs de transações e seus respectivos valores. 
* **Regra de Detecção**: Qualquer transação com valor superior a R$ 1.000,00 é marcada como uma anomalia (cor vermelha no gráfico).
* **Resultado**: O programa gera um gráfico de dispersão facilitando a identificação visual dos pontos fora da curva (outliers).

## 📈 Resultados
O projeto consegue separar com precisão transações comuns de tentativas de fraude ou erros operacionais, permitindo uma tomada de decisão rápida pela equipe de segurança financeira.
