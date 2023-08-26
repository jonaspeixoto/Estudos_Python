"""

Desafio 1:
Escreva um programa em Python que peça ao usuário para digitar um número inteiro. Em seguida, verifique se o número é positivo,
negativo ou igual a zero e exiba uma mensagem correspondente.

"""

# numero = int(input(('Digite um número inteiro: ')))
# while numero != 0:
#     if numero > 0:
#         print(f'O número {numero} é positivo ')
#     else:
#         print(f'O número {numero} é négativo ')
        
#     numero = int(input(('Digite um número inteiro: ')))
#     if numero == 0:
#         print(f'O número é zero')


"""

Desafio 2 - "Classificação de Números Inteiros (Versão Simplificada)":
Escreva um programa em Python que peça ao usuário para digitar três números inteiros separados por espaço. Em seguida, o programa deve classificar cada número digitado como positivo, negativo ou igual a zero e exibir uma mensagem correspondente.

Além disso, o programa deve calcular e exibir a seguinte informação adicional:

A soma dos números positivos.
O produto dos números negativos.

"""

# print('Digite 3 numeros inteiros ')
# numero1 = int(input(('')))
# numero2 = int(input(('')))
# numero3 = int(input(('')))

# soma_positivo = 0
# soma_negativo = 0

# if numero1 > 0:
#     print(f'O número {numero1} é positivo ')
#     soma_positivo += numero1
# else:
#     print(f'O número {numero1} é négativo ')
#     soma_negativo += numero1     


# if numero3 > 0:
#     print(f'O número {numero3} é positivo ')
#     soma_positivo += numero3
# else:
#     print(f'O número {numero3} é négativo ')
#     soma_negativo =+ numero3     

# if numero3 > 0:
#     print(f'O número {numero3} é positivo ')
#     soma_positivo += numero3
# else:
#     print(f'O número {numero3} é négativo ')
#     soma_negativo += numero3     


# print(f'Soma dos números positivos: {soma_positivo}')
# print(f'Soma dos números negativos: {soma_negativo}')

"""

Desafio 2.1 - "Classificação de Números Inteiros (Com funções)":
Escreva um programa em Python que peça ao usuário para digitar três números inteiros separados por espaço. Em seguida, o programa deve classificar cada número digitado como positivo, negativo ou igual a zero e exibir uma mensagem correspondente.

Além disso, o programa deve calcular e exibir a seguinte informação adicional:

A soma dos números positivos.
O produto dos números negativos.

"""


def soma_elementos(numero,soma_positivo, soma_negativo):
    if numero > 0:
        print(f'O número {numero} é positivo ')
        soma_positivo += numero
    else:
        print(f'O número {numero} é négativo ')
        soma_negativo += numero  

    return soma_positivo, soma_negativo

print('Digite 3 numeros inteiros ')
numero1 = int(input(('')))
numero2 = int(input(('')))
numero3 = int(input(('')))

soma_positivo = 0
soma_negativo = 0 

soma_positivo, soma_negativo = soma_elementos(numero1,soma_positivo, soma_negativo)
soma_positivo, soma_negativo = soma_elementos(numero2,soma_positivo, soma_negativo)
soma_positivo, soma_negativo = soma_elementos(numero3,soma_positivo, soma_negativo)

print(f'Soma positiva dos numeros: {soma_positivo}')
print(f'Soma negativa dos numeros: {soma_negativo}')

