# f-strings mais importantes, dá para colocar um padding
# {nome da variavel:(simbolo desejado)(ação)(quantas vezes)}
# {preco: >10} -> vai colocar 10 caracteres de espaço em branco do lado esquerdo
# = força o número a aparecer antes do 0
# Conversion flag -> vai aparecer depois

print(f'{10021.21:0=+10,.1f}') # Essas adições contam como caracteres