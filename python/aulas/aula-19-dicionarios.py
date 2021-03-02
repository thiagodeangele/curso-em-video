# Curso em Vídeo | Python 
# Aula 19 - Dicionários
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



# •••••••••••••••••••••••••••••••••••••••••••••••••••••• 
separador('Separa')
# ••••••••••••••••••••••••••••••••••••••••••••••••••••••

# Tupla = ()
# Listas = []
# Listas = list()
# Dicionários = {}
# Dicionários = dict()


dados = dict()
dados = {'nome' : 'Pedro', 'idade' : 25}
print(dados['nome'])
print(dados['idade'])

# Adicionar
dados['sexo'] = 'M'
print(dados)

# Remover
del dados['idade']
print(dados)


# •••••••••••••••••••••••••••••••••••••••••••••••••••••• 
separador('Separa')
# ••••••••••••••••••••••••••••••••••••••••••••••••••••••


filme = {'titulo' : 'Star Wars',
         'ano' : 1977,
         'diretor' : 'George Lucas'
         }

print(filme.values()) # 'Value' são os conteúdos
print(filme.keys()) # 'Keys' são os títulos
print(filme.items()) # Retorna tudo

for k, v in filme.items():
    print(f'O {k} é {v}')


# •••••••••••••••••••••••••••••••••••••••••••••••••••••• 
separador('Explicado às 16:20')
# ••••••••••••••••••••••••••••••••••••••••••••••••••••••


pessoas = { 
    'nome': 'Gustavo',
    'sexo': 'M',
    'idade': 22
    }

print(pessoas)
print(pessoas.values())
print(pessoas['nome'])
print(f'O {pessoas["nome"]} tem {pessoas["idade"]} anos')

for k in pessoas.keys():
    print(k)

for k in pessoas.values():
    print(k)

for k, v in pessoas.items():
    print(f'{k} = {v}')

del pessoas['sexo']
print(pessoas)

pessoas['nome'] = 'Leandro'
pessoas['peso'] = 98.5
print(pessoas)


# •••••••••••••••••••••••••••••••••••••••••••••••••••••• 
separador('Explicado às 21:50')
# ••••••••••••••••••••••••••••••••••••••••••••••••••••••

brasil = list()

estado1 = {
    'uf': 'Rio de Janeiro',
    'sigla': 'RJ'
}

estado2 = {
    'uf': 'São Paulo',
    'sigla': 'SP'
}

brasil.append(estado1)
brasil.append(estado2)

print(brasil)
print(brasil[1])
print(brasil[1]['sigla'])



# •••••••••••••••••••••••••••••••••••••••••••••••••••••• 
separador('Explicado às 25:10')
# ••••••••••••••••••••••••••••••••••••••••••••••••••••••

estado = dict()
brasil = list()

for c in range(0, 3):
    estado['uf'] = str(input('Unidade Federativa: ')).strip()
    estado['sigla'] = str(input('Sigla: ')).strip()
    print()
    brasil.append(estado.copy())
print(brasil)


print('\n••• ••• •••\n')

for estad in brasil:
    for k, v in estad.items():
        print(f'O campo {k} tem valor {v}')


print('\n••• ••• •••\n')


for estad in brasil:
    for v in estad.values():
        print(f'{v}', end=' ')
    print()