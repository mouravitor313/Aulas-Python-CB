from random import *

a = input('Digite o nome do aluno 1\n')
b = input('\nDigite o nome do aluno 2\n')
c = input('\nDigite o nome do aluno 3\n')
d = input('\nDigite o nome do aluno 4\n')

names = f'{a} {b} {c} {d}'.split()

print(f'\nO escolhido foi o: {choice(names)}')

shuffle(names)
print(f'\n{names}')



