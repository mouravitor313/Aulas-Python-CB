d = float(input('Digite a distância percorrida pelo carro: '))

if d <= 200:
    print(f'Deverá ser cobrado o valor de: RS{d*0.5}')
else:
    print(f'Deverá ser cobrado o valor de: RS{d*0.45}')