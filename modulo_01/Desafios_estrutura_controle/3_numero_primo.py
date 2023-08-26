"""
Desafio 5 - "Verificação de Números Primos":
Escreva um programa em Python que solicite ao usuário um número inteiro positivo e verifique se ele é um número primo ou não.
Um número primo é aquele que é divisível apenas por 1 e por ele mesmo.

"""

numero = int(input('Digite um numero'))
divisores = 0 

for i in range(2,numero + 1):
    if numero % i == 0:
        divisores += 1

if divisores == 1:
    print('Numero é primo')
else:    
    print('Numero não é primo')
    