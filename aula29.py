# O try catch de outras linguagens é try except aqui
# try -> executar, except ->  capturar o erro
# Estourar uma exceção - ver um erro
# if e try são controladores de fluxo, contudo o uso do try evita a interrupção

num_str = input('Vou dobrar o número que vc digitar!')

try: #Não é a forma correta de se usar um try
    num_float = float(num_str)
    print(f'O dobro do número {num_str} é {num_float * 2:.2f}')
except:
    print('Não foi digitado um número')