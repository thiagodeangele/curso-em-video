# Curso em Vídeo | Python 
# Aula 21 - Funções - Parte 02
# Prof. Gustavo Guanabara


def separador(texto): 
    
    """
    Formata uma divisão entre assuntos.
    Parametro [texto]: Recebe uma string
    Retorno: Sem retorno

    """

    corAzul = '\033[34m'
    corFecha = '\033[m'  

    print(f'\n{corAzul}••• {texto.upper()} ••• ••• ••• ••• ••• ••• ••• ••• ••• •••{corFecha}\n')

def div():  

    corAmarelo = '\033[33m'
    corVermelho = '\033[31m'
    corAzul = '\033[34m'
    corVerde = '\033[32m'
    corRoxo = '\033[35m'
    corCiano = '\033[36m'
    corCinza = '\033[37m'
    corFecha = '\033[m'   
    
    print(f'\n{corAmarelo}... ... ...{corFecha}\n')

def somar(a = 0, b= 0, c = 0):
    
    """
    Parâmetros opcionais.
    """
    
    s = a + b + c
    print(f'A soma vale {s}')

def teste():
    x = 8
    print(f'Na função teste n vale {n}')
    print(f'Na função teste x vale {x}')

def teste2(b):
    a = 8
    b += 4
    c = 2
    print(f'A dentro vale {a}')
    print(f'B dentro vale {b}')
    print(f'C dentro vale {c}')

def somar2(a = 0, b = 0, c = 0):
    s = a + b + c
    return s

def fatorial(num = 1):
    f = 1
    for c in range(num, 0 , -1):
        f *= c
    return f

def par(n = 0):
    if n % 2 == 0:
        return True
    else:
        return False


# -------------------------------------------------------
separador('Help')
# -------------------------------------------------------

# Mostra no console um texto de ajuda com algumas definições
# sobre a função.

print(input.__doc__)

div() # ---

help(input)



# -------------------------------------------------------
separador('Parâmetros Opcionais')
# -------------------------------------------------------

# Pode-se colocar, ao lado da variável dentro da função, um valor para que, caso a variável
# não existe, ele assuma.

somar(3, 2, 5)
somar(8, 4) # Terceiro número iformado na função como opcional
somar()



# -------------------------------------------------------
separador('Escopo de Variáveis') #21:48
# -------------------------------------------------------

# Local em que uma variável vai ou não existir.

# ESCOPO GLOBAL
# Variável funciona em todo o espaço

# ESCOPO LOCAL
# Variável criada dentro da função, vale só na função
# Se criar uma variável, dentro da função, com o mesmo nome de uma variável GLOBAL,
# a variável só valerá dentro da função.

n = 2
print(f'No programa principal n vale {n}')
teste()

div() # ---

a = 5
teste2(a)
print(f'A fora vale {a}')



# -------------------------------------------------------
separador('Retornando Valores // RETURN') #31:43
# -------------------------------------------------------

somar2(3, 2, 5)
somar2(2, 2)
somar2(6)

r1 = somar2(3, 2, 5)
r2 = somar2(2, 2)
r3 = somar2(6)

print(f'Meus cálculos deram {r1}, {r2} e {r3}')
print(f'Meus cálculos deram {somar2(3, 2, 5)}, {somar2(2, 2)} e {somar2(6)}')




# -------------------------------------------------------
separador('Parte Prática') #36:00
# -------------------------------------------------------

n = int(input('Digite um número: '))
print(f'O fatorial de {n} é igual a {fatorial(n)}')

f1 = fatorial(5)
f2 = fatorial(4)
f3 = fatorial()
print(f'Os resultados são {f1}, {f2} e {f3}')


div() # ---


num = int(input('Digite um número: '))
if par(num):
    print('É PAR!')
else:
    print('É ÍMPAR!')