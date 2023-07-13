n1 = float(input('Digite a primeira nota do aluno:\n'))
n2 = float(input('Digite a segunda nota do aluno:\n'))
n3 = float(input('Digite a terceira nota do aluno\n'))
n4 = float(input('Digite a quarta nota do aluno:\n'))

m = (n1 + n2 + n3 + n4) / 4

print(f'A média do aluno é: {m}')

if m < 5.0:
    print('Reprovado')
elif m >= 7.0:
    print('Aprovado')
else:
    print('Recuperação')