# p = int(input('Idade: '))
# cont = 0

# while(cont!=p):
#     cont = cont + 1
#     print(cont)

#sexo = ''

# while True:
#     sexo = input('Sexo: [F/M]').upper()
#     if sexo == 'M' or sexo == 'F':
#         print(f'Você é {sexo}')
#         break
#     else:
#         print('Digite um valor válido!')

'''
dicionario = {}

while(True):
    s = input('Deseja encerrar o programa? [Sim/Não] ').capitalize()
    if 'S' in s:
        break
    elif 'N' in s:
        name = input('Digite o teu nome: ').capitalize()
        dicionario[name]
        age = int(input('Digite a tua idade: '))
        dicionario[name] = age
        genre = input('Digite o teu genêro[M/F]: ').upper()
        dicionario[name] = genre
        print(dicionario)
    else:
        print('Digite uma resposta válida!')
'''

f = int(input('Digite um número para dobrar: '))

def dobra(x = 0): # o x (ou qualquer nome só informa que a função recebe um parametro)
    return x * 2

# não precisa por x na chamada da função!!!
print(dobra(f))