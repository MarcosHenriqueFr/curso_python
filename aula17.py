# Python foca muito na identação do código

ensolarado = True
chuva = False
animado = True

# Hierarquia de if's normalmente
if ensolarado:
    print('Hojé é um dia de sol') #Executada primeiro
elif chuva:
    # ... -> Usado de placeholder
    print('Hojé um dia de chuva')
elif animado:
    # pass -> Usado de placeholder
    print('Hoje é um dia feliz')
else: 
    print('Nenhuma das condições foram atendidas!')

if 10 == 10:
    print('10 é igual a 10')