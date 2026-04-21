import pandas as pd
import matplotlib.pyplot as plt

# 1. Dados de exemplo
data = {
    'transacao': range(1, 11),
    'valor': [10.5, 15.2, 12.0, 5000.0, 14.2, 11.0, 13.5, 8000.0, 10.0, 12.5]
}
df = pd.DataFrame(data)

# 2. Definindo limite para anomalias
limite = 1000
df['anomalia'] = df['valor'] > limite

# 3. Criando a visualização
plt.figure(figsize=(10, 6))
cores = ['blue' if not x else 'red' for x in df['anomalia']]

plt.scatter(df['transacao'], df['valor'], c=cores, s=100)
plt.axhline(y=limite, color='r', linestyle='--', label='Limite de Alerta')

plt.title('Detecção de Anomalias em Transações Financeiras')
plt.xlabel('Número da Transação')
plt.ylabel('Valor (R$)')
plt.legend()

# Salva o gráfico como imagem para o portfólio
plt.savefig('resultado_anomalias.png')
print("Análise concluída. Imagem 'resultado_anomalias.png' gerada.")
print(df[df['anomalia'] == True])
