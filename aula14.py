# Método format

a = 'A'
b = 'B'
c = 1.1
formato = 'a={nome1} b={nome2} c={nome3:.2f}'.format(
    nome1=a,
    nome2=b, 
    nome3=c
)

#parâmetros nomeados 
#o método "joga" os argumentos de acordo com indice
#out of range - Buscar algo que acabou

print(formato)