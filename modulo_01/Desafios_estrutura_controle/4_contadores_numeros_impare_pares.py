"""
Desafio 6 - "Contador de Números Pares e Ímpares":
Escreva um programa em Python que peça ao usuário para digitar uma sequência de números inteiros separados por espaço. 
Em seguida, o programa deve contar quantos números pares e quantos números ímpares foram digitados.

"""

entrada = input('Digite uma sequencia de numeros separados por espaço: ')
numeros = map(int, entrada.split())
# numeros = [int(n) for n in entrada.split()]

quantidade_numeros_pares = 0
quantidade_numeros_impares = 0

for numero in numeros:
    if numero % 2 == 0:
        quantidade_numeros_pares += 1

    else:
        quantidade_numeros_impares +=1

print(f'Numeros pares: {quantidade_numeros_pares}. Nuemros impares: {quantidade_numeros_impares}')