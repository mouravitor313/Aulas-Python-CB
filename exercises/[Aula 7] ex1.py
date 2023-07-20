from random import randint

def main():
    cont = 0
    while(True):
        n = randint(1,10)
        while(True):
            e = int(input('Adivinhe o número: '))
            if e == n:
                print(f'\nVocê adivinhou!\n{n}\nVocê tentou {cont} vezes')
                break
            else:
                cont = cont + 1
        s = input('Deseja encerrar?[Sim/Não]: ').capitalize()
        if 'N' in s:
            pass
        elif 'S' in s:
            break
        else:
            print('Escolha inválida!')


main()


