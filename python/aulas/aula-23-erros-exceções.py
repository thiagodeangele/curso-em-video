# Curso em Vídeo | Python 
# Aula 23 - Erros e Exceções
# Prof. Gustavo Guanabara


try:
    a = int(input('Numerador: '))
    b = int(input('Denominador: '))
    r = a / b

except Exception as erro:    
    print(f'Erro encontrado foi {erro.__class__}')
except (ValueError, TypeError):
    print('Problema com dados')
except ZeroDivisionError:
    print('Problema com divisão por zero')
except KeyboardInterrupt:
    print('Usuário não informou os dados')

else:
    print(f'O resultado é {r:.1f}')

finally:
    print(f'Volte sempre')