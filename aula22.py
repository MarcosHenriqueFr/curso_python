# Operador lógico OR

entrada = input('[E]ntrar [S]air: ').upper()
senha_digitada = input('Informe a sua senha: ') or 'Sem senha!' #pequena validação

senha_permitida = '12345'

#se tiver mais de um operador pode ficar ambíguo, usar parênteses para evitar confusão
if ((entrada == 'E' or entrada == 'e') and senha_digitada == senha_permitida): 
    print('Entrou no sistema!')
elif (entrada == 'S'): 
    print('Saiu do sistema!')
else:
    print('Senha ou ação incorretos')