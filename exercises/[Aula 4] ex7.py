# faça um programa que leia 3 retas de um usuario e diga se elas podem formar um triangulo

'''Por exemplo, dados os segmentos AB = 16 cm, CD = 20 cm e EF = 30 cm,
é possível usá-los para construir um triângulo, pois as somas abaixo são verdadeiras:
16 + 20 = 36 > 30. 16 + 30 = 46 > 20.'''



a = 16
b = 20
c = 30

if (a + b) > c and (a + c) > b:
    print('É um triângulo!!!!!! ^-^')