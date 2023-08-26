"""
"Conversor de Notas":
Escreva um programa em Python que peça ao usuário para digitar a nota de um aluno 
em uma escala de 0 a 100. Em seguida, o programa deve verificar e exibir a nota correspondente em conceito, 
de acordo com a seguinte tabela:

"""

print('Escolha uma opçao: \n1 - Converter nota para conceito \n2 - Converter conceito para faixa de notas')
opcao = int(input(''))

if opcao == 1:
    nota = int(input('Digite sua nota: '))

    if nota >= 90 and nota <= 100:
        print(f'Conceito A ')
    if nota >= 80 and nota <= 89:
        print(f'Conceito B ')
    if nota >= 70 and nota <= 79:
        print(f'Conceito C ')
    if nota >=60 and nota <= 69:
        print(f'Conceito D ')
    if nota < 60:
        print(f'Conceito F ')

if opcao == 2:
    conceito = input('Digite conceito : ')
    if conceito == 'A':
        print(f'Faixa de notas correspondente: 90 a 100')
    elif conceito == 'B':
        print(f'Faixa de notas correspondente: 80 a 89')
    elif conceito == 'C':
        print(f'Faixa de notas correspondente: 70 a 79')
    elif conceito == 'D':
        print(f'Faixa de notas correspondente: 60 a 69')
    else:
        print(f'Faixa de notas correspondente: 60-')
