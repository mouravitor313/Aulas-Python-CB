'''Para encontrar o termo n de uma progressão aritmética,
é possível utilizar a fórmula do termo geral da progressão aritmética,
que é a n = a 1 + (n – 1)r1. Nessa fórmula, a n é o termo que se deseja encontrar,
a 1 é o primeiro termo da progressão e r é a razão da progressão aritmética1.
Outra fórmula que pode ser utilizada para encontrar os termos de uma progressão aritmética é a n = a + (n-1)d,
onde a é o primeiro termo da progressão e d é a diferença comum2.'''


# a1 = int(input('Digite o primeiro termo: '))
a1 = int(input('Digite o termo: '))
r = int(input('Razão da PA: '))
for i in range(1,21):
    an = a1 + (i-1)*r
    print(an)