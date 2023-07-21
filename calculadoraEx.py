print('''*****************
*  Calculadora  *
*****************''')

from os import system

# Operações
soma = ''
sub = ''
div = ''
mult = ''

# Váriaveis para receber as escolhas do usuário
n = 0
n1 = 0
op = 'a'

print('''Bem vindo a calculadora!!!!
Digite os sinais das operações no Python para selecionar a operação
Digite o sinal de igual "=" para selecionar o resultado da operação anterior e fazer um calculo com ela
Digite "C" para usar a função clear
Para encerrar, apenas aperte enter\n ''')

def somar(x, x2):
	s = x + x2
	return s

def subtrair(x, x2):
	s = x - x2
	return s

def multi(x, x2):
	s = x * x2
	return s

def divi(x, x2):
	s = x / x2
	return s

def maior(x, x2):
	if x > x2:
		return x
	if x2 > x:
		return x


while True:
    n = int(input('n: '))
    while (op != ''):
        op = input('Escolha uma operação: ')
        if op == '+':
            while(True):
                n1 = int(input('n: '))
                re = somar(n,n1)
                print(f'O resultado foi: {re}')
                op = input('Digite a operação: ')
                if op == '=':
                    n = re
                    print(n)
                    break
                else:
                    break
        if op == '-':
            while(True):
                n1 = int(input('n: '))
                re = subtrair(n,n1)
                print(f'O resultado foi: {re}')
                op = input('Digite a operação: ')
                if op == '=':
                    n = re
                    print(n)
                    break
                else:
                    break