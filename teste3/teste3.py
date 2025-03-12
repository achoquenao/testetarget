import json
import os

diretorio_atual = os.path.dirname(os.path.abspath(__file__))
caminho_arquivo = os.path.join(diretorio_atual, 'dados.json')

with open(caminho_arquivo, 'r') as file:
    dados = json.load(file)

faturamento_diario = [dia['valor'] for dia in dados]

faturamento_sem_zeros = [valor for valor in faturamento_diario if valor > 0]

menor_faturamento = min(faturamento_sem_zeros)
maior_faturamento = max(faturamento_sem_zeros)

media_mensal = sum(faturamento_sem_zeros) / len(faturamento_sem_zeros)

dias_acima_da_media = sum(1 for faturamento in faturamento_diario if faturamento > media_mensal)

print(f"Menor valor de faturamento: R$ {menor_faturamento:.2f}")
print(f"Maior valor de faturamento: R$ {maior_faturamento:.2f}")
print(f"Número de dias com faturamento superior à média mensal: {dias_acima_da_media}")