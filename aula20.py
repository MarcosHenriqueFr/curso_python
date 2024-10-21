valor1 = input('Insira um valor: ')
valor2 = input('Insira outro valor: ')

if valor1 > valor2:
    print(f'{valor1=} é maior que o {valor2=}')
elif valor2 > valor1:
    print(f'{valor2=} é maior que o valor {valor1=}')
elif valor1 == valor2:
    print(f'O {valor1=} é igual ao {valor2=}')
else: 
    print('Não foi possível realizar a comparação')