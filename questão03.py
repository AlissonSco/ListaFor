nn = int(input('Digite um número: '))
cont = 0
for a in range(0, nn+1):
    if a%2 ==0:
        cont = cont+a

print(cont)