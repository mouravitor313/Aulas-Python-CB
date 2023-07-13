v = float(input('Qual é o valor da casa? ')) # valor
s = float(input('Digite o salário do comprador: ')) # salário
t = int(input('Qual é a duração das parcelas? ')) # tempo

p = v / (t * 12) # parcelas

trinta = s*0.3

if p / s > trinta:
    print('Emprestimo negado.)')
else:
    print('Emprestimo aceito')