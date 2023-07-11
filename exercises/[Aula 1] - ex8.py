n1 = int(input('Digite um número:\n'))
print(f'Para saber se o número é par ou ímpar, precisamos fazer um calculo que o resultado mostrado irá definir o resultado.\nAbaixo aparecerá um número, caso seja 0, é par. Se for 1, é ímpar.\n{n1%2}')

print('Se o if estivesse liberado:')
if n1%2 == 1:
    print('É ímpar!')
else:
    print('É par!')
