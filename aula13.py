# Formatação de strings(introdução)
# f antes da string permite usar variáveis em uma string

nome = "Marcos"
altura = 1.82
peso = 80.5
imc = peso / altura ** 2

# f-strings
linha_1 = f'{nome} tem {altura:.2f} de altura'
linha_2 = f'pesa {peso} quilos e seu IMC é {imc:.2f}'
# var:.quantidade_linhas + f -> casas decimais
# var,.quantidade_casas + f -> formatação monetária

print(linha_1)
print(linha_2)
