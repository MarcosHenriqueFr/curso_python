# Operador Lógico AND(E) mais de uma proposição
# Falsy's padrões: 0 0.0 '', tem o None que é inexistente
# Avaliação de curto circuito em booleanos para economizar recursos

entrada = input('[E]ntrar [S]air: ').upper()
senha_digitada = input('Informe a sua senha: ')

senha_permitida = '12345'

if (entrada == 'E' and senha_digitada == senha_permitida):
    print('Entrou no sistema!')
elif (entrada == 'S'): 
    print('Saiu do sistema!')
else:
    print('Senha ou ação incorretos')