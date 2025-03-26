nn = int(input('Digite um número: '))
cont = 0
for a in range(1, nn):
    if (a%3 == 0) or (a%5==0):
        cont = cont+a
print(cont)