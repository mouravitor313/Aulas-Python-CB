v1 = int(input('Digite um valor: '))
v2 = int(input('Digite um outro valor: '))
v3 = int(input('Agora digite mais um outro valor: '))

if v1 > v2 and v1 > v3:
    print (f'O maior é: {v1}')
    if v2 > v3:
        print (f'O menor é: {v3}')
    else:
        print (f'O menor é: {v2}')

elif v2 > v1 and v2 > v3:
    print (f'O maior é: {v2}')
    if v1 > v3:
        print (f'O menor é: {v3}')
    else:
        print (f'O menor é: {v1}')

elif v3 > v1 and v3 > v2:
    print (f'O maior é: {v3}')
    if v1 > v2:
        print (f'O menor é: {v2}')
    else:
        print (f'O menor é: {v1}')

