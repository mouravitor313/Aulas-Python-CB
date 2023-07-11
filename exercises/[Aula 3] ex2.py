from math import hypot

cO = float(input('Digite o comprimento do cateto oposto:\n'))
cA = float(input('Digite o comprimento do cateto adjacente:\n'))

# c^2 = a^2 + b^2

h = hypot(cO, cA)
print(f'O comprimento da hipotenusa é: {h}')