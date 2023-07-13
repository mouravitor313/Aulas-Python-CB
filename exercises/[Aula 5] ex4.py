a = int(input('Digite o ano do teu nascimento: '))
idade = 2023 - a

if idade == 18:
    print('Você está na idade para se alistar!')
elif idade < 18:
    print(f'Você ainda é muito novo para se alistar. Espere mais {18-idade} anos para se alistar')
else:
    print('Você já passou da época de se alistar')