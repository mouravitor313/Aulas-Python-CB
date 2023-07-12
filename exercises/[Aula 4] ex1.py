from random import choice

cntrl = input('Deseja brincar de adivinhar? ').upper()

if cntrl == 'S':
    n = choice(range(0, 6))
    num = int(input('Adivinhe o número: '))
    if num == n:
        print('Você acertou!')
    else:
        print('Você errou!')
else:
    print('Tchau')

