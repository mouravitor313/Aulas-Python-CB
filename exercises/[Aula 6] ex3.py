cont = 0
t = 0

for i in range(1, 500):
    if i % 3 == 0:
        cont = cont + 1
        t = t + i
print(t,cont)
# i % 10 == 0