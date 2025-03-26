nn = int(input("Digite o valor de n: "))
for i in range(nn+1):
    fatorial = 1
    j = 1
    while j <=i:
        fatorial = fatorial*j
        j += 1
    print(f"O fatorial de {i} é {fatorial}")