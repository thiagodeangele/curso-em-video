# Curso em Vídeo | Python 
# Aula 17 - Listas - Parte 01
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
  


lanche = ['hamburger', 'suco', 'pizza', 'pudim']
print(lanche)

lanche[3] = 'sorvete'
print(lanche)

lanche.append('cookie')
print(lanche)

lanche.insert(0, 'cachorro quente') #posição, item
print(lanche)

del lanche[3]
print(lanche)

lanche.pop(3) # Normalmente deleta o último, mas pode também passar o índice
print(lanche)

lanche.remove('cookie') # Remove pelo conteúdo
print(lanche)

if 'pizza' in lanche:
    lanche.remove('pizza')
print(lanche)


valores = list(range(4, 11))
print(valores)

valores = [8, 2, 5, 4, 9, 3, 0]
valores.sort()
print(valores)

valores = [8, 2, 5, 4, 9, 3, 0]
valores.sort(reverse = True)
print(valores)

valores = list(range(4, 11))
print(len(valores))



# •••••••••••••••••••••••••••••••••••••••••••••••••••••• 
separador('Separa')
# ••••••••••••••••••••••••••••••••••••••••••••••••••••••



num = [2, 5, 9, 1]
num[2] = 3
num.append(7)
num.sort(reverse = True)
num.insert(2, 2)
if 5 in num:
    num.remove(5)
else:
    print('Não achei o número 4')
print(num)
print(f'Essa lista tem {len(num)} elementos.')



# •••••••••••••••••••••••••••••••••••••••••••••••••••••• 
separador('Separa')
# ••••••••••••••••••••••••••••••••••••••••••••••••••••••



val = list()
val.append(5)
val.append(9)
val.append(4)

for cont in range(0, 5):
    val.append(int(input('Digite um valor: ')))

for v in val:
    print(f'{v}...')

for c, v in enumerate(val):
    print(f'Na posição {c} encontrei o valor {v}')
print('Cheguei ao final da lista')



# •••••••••••••••••••••••••••••••••••••••••••••••••••••• 
separador('Separa')
# ••••••••••••••••••••••••••••••••••••••••••••••••••••••



a = [2, 3, 4, 7]
b = a[:] #Cria uma cópia de A em B
b[2] = 8

print(f'Lista A: {a}')
print(f'Lista B: {b}')