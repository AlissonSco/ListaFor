soma = 0
for n in range(1, 100+1):
    if n > 1:
        for i in range(2, n):
            if n % i == 0:
                break
        else:
            soma += n
print(f'A soma e: {soma}')