import pandas as pd
import numpy as np

# 1. Criando dados fictícios para o projeto
data = {
    'id_transacao': range(1, 11),
    'valor': [10.50, 15.00, 12.00, 5000.00, 14.20, 11.00, 13.50, 8000.00, 10.00, 12.50],
    'tempo_dia': [10, 11, 12, 3, 14, 15, 16, 2, 18, 19] # Hora da transação
}

df = pd.DataFrame(data)

print("--- Primeiras linhas do dataset ---")
print(df.head())

# 2. Uma lógica simples de detecção (Regra de Negócio)
# Vamos considerar anomalia qualquer valor acima de 1000 reais
# ou transações feitas na madrugada (entre 0h e 5h)
limite_valor = 1000

print(f"\nBuscando transações acima de R$ {limite_valor} ou em horários suspeitos...")

anomalias = df[(df['valor'] > limite_valor) | (df['tempo_dia'] < 5)]

print("\n--- Anomalias Detectadas ---")
print(anomalias)
