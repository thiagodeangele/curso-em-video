# Curso em Vídeo | Python 
# Aula 20 - Funções
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

def mensagem(msg):
    print('-' * 30)
    print(f'{msg:^30}')
    print('-' * 30)


mensagem(('Curso em Vídeo').upper())
mensagem(('Python é muito bom!').title())


# •••••••••••••••••••••••••••••••••••••••••••••••••••••• 
separador('Separa')
# ••••••••••••••••••••••••••••••••••••••••••••••••••••••


def soma (num1, num2):
    print(f'[A] = {num1} | [B] = {num2}')
    s = num1 + num2
    print(f'A soma de [A] + [B] = {s}')
    print()


soma(4, 5)
soma(8, 9)
soma(0, 1)
soma(num2 = 0, num1 = 1)



# •••••••••••••••••••••••••••••••••••••••••••••••••••••• 
separador('Separa')
# ••••••••••••••••••••••••••••••••••••••••••••••••••••••



def contador(*num):
    
    for valor in num:
        print(f'{valor} ', end='')
    print()
    
    tamanho = len(num)
    print(f'Recebi os valores {num} que são ao todo {tamanho} números')

contador(7, 5, 3, 1, 4)
contador(2, 8, 7)



# •••••••••••••••••••••••••••••••••••••••••••••••••••••• 
separador('Separa')
# ••••••••••••••••••••••••••••••••••••••••••••••••••••••


def dobra(lista):
    posicao = 0
    while posicao < len(lista):
        lista[posicao] *= 2
        posicao += 1


valores = [6, 3, 9, 1, 0, 2]
dobra(valores)
print(valores)


