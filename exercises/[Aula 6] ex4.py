n = int(input('Digite um número que será multiplicado: '))
f = int(input('Até qual número? '))

f = f + 1

for i in range(1,f):
     print(f'{n}X{i} = {n*i}')

