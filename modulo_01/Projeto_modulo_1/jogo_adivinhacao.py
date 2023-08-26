"""
Desafio: Mini Jogo de Adivinhação

Descrição:

Neste desafio, você criará um mini jogo de adivinhação em que o programa 
escolhe um número aleatório entre 1 e 100, e o jogador deve tentar adivinhar qual é esse número.

"""

from random import randint 


while True:
    number = randint(0,101)

    win = False
    attempt = 0

    while win == False:
        try:
            choice = int(input('Escolnha um numero'))
        except ValueError:
            print('Por favor, insira somente números inteiros.')
            continue
        
        attempt += 1
        
        if choice < number:
            print('Palpite muito baixo. Tente novamente!')
        elif choice > number:
            print('Palpite muito alto. Tente novamente!')
        elif choice == number:
            print(f'Parabéns! Você acertou o número em {attempt} tentativas!')
            win = True

    print(f'o numero era {number}')
    codicion = input('jogar novamente ?')
    print('Digite s para jogar novamente e n para não !')
    if codicion == 'n':
        exit()



