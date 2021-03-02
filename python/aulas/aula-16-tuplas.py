# Curso em Vídeo | Python 
# Aula 16 - Tuplas
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
    

lanche = ('Hambúrger', 'Suco', 'Pizza', 'Pudim', 'Batata Frita')
print(lanche)
print(lanche[-2])
print(lanche[-2:])
print(lanche[2])
print(lanche[1:3])
print(lanche[2:])
print(lanche[:2])

# •••••••••••••••••••••••••••••••••••••••••••••••••••••• 
separador('Separa')
# ••••••••••••••••••••••••••••••••••••••••••••••••••••••

print(len(lanche))
print(sorted(lanche))


# •••••••••••••••••••••••••••••••••••••••••••••••••••••• 
separador('Separa')
# ••••••••••••••••••••••••••••••••••••••••••••••••••••••


for comida in lanche:
    print(f'Eu vou comer {comida}')


# •••••••••••••••••••••••••••••••••••••••••••••••••••••• 
separador('Separa')
# ••••••••••••••••••••••••••••••••••••••••••••••••••••••


for cont in range (0, len(lanche)):
    print(f'Eu vou comer {lanche[cont]} na posição {cont}')


# •••••••••••••••••••••••••••••••••••••••••••••••••••••• 
separador('Separa')
# ••••••••••••••••••••••••••••••••••••••••••••••••••••••


for posicao, comida in enumerate(lanche):
    print(f'Eu vou comer {comida} na posição {posicao}')


# •••••••••••••••••••••••••••••••••••••••••••••••••••••• 
separador('Separa')
# ••••••••••••••••••••••••••••••••••••••••••••••••••••••


a = (2, 5, 4)
b = (5, 8, 1, 2)
c = b + a
print(c)
print(len(c))
print(c.count(5))
print(c.index(4))
print(c.index(5, 1)) #Começa a procurar na posição 1
print(max(c))


# •••••••••••••••••••••••••••••••••••••••••••••••••••••• 
separador('Separa')
# ••••••••••••••••••••••••••••••••••••••••••••••••••••••


pessoa = ('Gustavo', 39, 'M', 99.88)
print(pessoa)
print(pessoa[2])
del(pessoa)