from os import system
from time import sleep

lista = []

while True:
    for i in range(1, 11):
        lista.append('*')
        print(lista)
        sleep(0.1)
    for i in range(1, 11):
        lista.pop()
        print(lista)
        sleep(0.1)
#    system('cls')
