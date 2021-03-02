# Curso em Vídeo | Python 
# Aula 18 - Listas - Parte 02
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


dados = list()
dados.append('Pedro')
dados.append(25)

print(dados[0])



# •••••••••••••••••••••••••••••••••••••••••••••••••••••• 
separador('Separa')
# ••••••••••••••••••••••••••••••••••••••••••••••••••••••



dados1 = ['Maria', 19]
dados2 = ['João', 32]

pessoas = list()
pessoas.append(dados[:]) #Copiou a lista total com [:]
pessoas.append(dados1[:]) #Copiou a lista total com [:]
pessoas.append(dados2[:]) #Copiou a lista total com [:]

print(pessoas[1])



# •••••••••••••••••••••••••••••••••••••••••••••••••••••• 
separador('Separa')
# ••••••••••••••••••••••••••••••••••••••••••••••••••••••



pessoas = [['Pedro', 25], ['Maria', 19], ['João', 32]]
print(pessoas)
print(pessoas[0][0]) # Pedro
print(pessoas[1][1]) # 19
print(pessoas[2][0]) # João
print(pessoas[1]) # ['Maria', 19]



# •••••••••••••••••••••••••••••••••••••••••••••••••••••• 
separador('Separa')
# ••••••••••••••••••••••••••••••••••••••••••••••••••••••



teste = list()
teste.append('Gustavo')
teste.append(40)

galera = list()
galera.append(teste[:])

teste[0] = 'Maria'
teste[1] = 22
galera.append(teste[:])
print(galera)


# •••••••••••••••••••••••••••••••••••••••••••••••••••••• 
separador('Separa')
# ••••••••••••••••••••••••••••••••••••••••••••••••••••••



galera = [['João', 19], ['Ana', 33], ['Joaquim', 13], ['Maria', 33]]

for pessoa in galera:
    print(f'{pessoa[0]} tem {pessoa[1]} anos de idade.')



# •••••••••••••••••••••••••••••••••••••••••••••••••••••• 
separador('Separa')
# ••••••••••••••••••••••••••••••••••••••••••••••••••••••


galera = list()
dado = list()
totalMaior = totalMenor = 0

#Este bloco serve para mandar os dados da variável DADO para GALERA
for c in range (0, 3):
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade: ')))
    galera.append(dado[:])
    dado.clear()

#Este bloco passa por todas pessoas e faz a verificação
for pessoa in galera:
    if pessoa[1] >= 21:
        print(f'{pessoa[0]} é maior de idade')
        totalMaior += 1
    else:
        print(f'{pessoa[0]} é menor de idade')
        totalMenor += 1

print(f'Temos {totalMaior} maiores de idade e {totalMenor} menores de idade')