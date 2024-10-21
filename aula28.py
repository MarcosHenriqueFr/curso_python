'''
Pedir para o usuário digitar um nome
pedir uma idade
Caso forem digitados, exibir:
    Seu nome é nome
    Seu nome invertido é nome invertido
    Seu nome contém ou não espaços
    Seu nome tem n letras
    A primeira letra do seu nome é letra
    A última letra do seu nome é letra

Se não forem escritos nome e idade, exibir:
    Desculpa você deixou campos vazios
'''

nome = input('Digite o seu nome: ')
idade = input('Digite a sua idade: ')

if((not idade) or (not nome)):
    print('Desculpa, você deixou campos vazios.')
else:
    print(f'Seu nome é {nome}')
    print(f'Seu nome invertido é {nome[::-1]}')
    
    if(' ' in nome):
        print('Seu nome contém espaços!')
    else:
        print('Seu nome não contém espaços!')

    print(f'Seu nome tem {len(nome)} letras')
    print(f'A primeira letra do seu nome é {nome[0]}')
    print(f'A última letra do seu nome é {nome[-1]}')