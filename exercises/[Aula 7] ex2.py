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



while (op != ''):
    op = input('Escolha uma operação (Aperte enter para sair): \n+ para somar\n- para subtrair\n* para multiplicar\n/ para dividir\n> para ver se um número é maior que o outro\n')
    if op == '+':
	    n = int(input('n: '))
        n1 = int(input('n: '))
        somar(n, n1)