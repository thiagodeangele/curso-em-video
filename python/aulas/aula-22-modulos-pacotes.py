# Curso em Vídeo | Python 
# Aula 22 - Módulos e Pacotes
# Prof. Gustavo Guanabara


def sessao(texto): 
    
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
    
def fatorial(n, show=False):

    """
    Calcula o Fatorial de um numero.
    
    Parametro [n]       O numero a ser calculado.
    -------------------------------------------------------
    Parametro [show]    Opcional - Mostra ou nao a conta.
    -------------------------------------------------------
    Return:             O valor fatorial de um numero n.
    -------------------------------------------------------
    """
   
    f = 1
    for c in range (n, 0, -1):
        f *= c
    return f


# -------------------------------------------------------
sessao('Modularização')
# -------------------------------------------------------

num = int((input('Número: ')))
fat = fatorial(num)

print(fat)