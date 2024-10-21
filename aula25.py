# Interpolação básica em python -> Mesmo feito com format, IGUAL EM C 
# Hexadecimal -> x e X, os placeholders se referem aos tipos
# f-strings, format e interpolação -> escolha uma delas para ficar mais fácil

nome = 'João'
preco = 10021.7262562
interpolacao = '%s, o preço total é R$%.2f' %(nome, preco)

print(interpolacao)
print('O hexadecimal de %d é %04X' %(120, 120))