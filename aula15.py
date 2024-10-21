#Função Input(solicita dados do usuário)
#para na linha e não finaliza o programa

# nome = input('Qual o seu nome? ') #Só sai no tipo string
# print(f'O seu nome é {nome}') #var= -> mostra o valor que tem em uma variável

numero1 = float(input('Digite um número: ')) #Sem checagem
numero2 = float(input('Digite outro número: '))

soma = numero1 + numero2

print(f'A soma dos números resultou em {soma:.2f}')

