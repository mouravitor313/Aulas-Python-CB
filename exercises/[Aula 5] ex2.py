'''Passos de conversão:
Divida o número por 2.
Obtenha o quociente inteiro para a próxima iteração.
Obtenha o resto do dígito binário.
Repita as etapas até que o quociente seja igual a 0.
Exemplo 1
Converta 13em binário:

Divisão
por 2	Quociente	Restante	Mordeu #
13/2	6	        1	        0
6/2	    3	        0	        1
3/2	    1	        1	        2
1/2	    0	        1	        3
Então 13 = 1101 2'''


n = int(input('Digite um número inteiro:\n'))
c = input('\nQual será a base da conversão?\n1 para binário\n2 para octal\n3 para hexadecimal\n')


if c == '1':
    print(bin(n))

elif c == '2':
    print(oct(n))

elif c == '3':
    print(hex(n))

else:
    print('Opção inválida!')