n1 = int(input('Digite um numero: '))
for num in range(0, n1 + 1):
    soma_dos_digitos = 0
    quantidade_digitos = 0
    num_copia = num

    while num_copia > 0:
        quantidade_digitos = quantidade_digitos + 1
        num_copia = num_copia // 10
    num_copia = num

    while num_copia > 0:
        digito = num_copia % 10
        soma_dos_digitos = soma_dos_digitos + (digito ** quantidade_digitos)
        num_copia = num_copia // 10
        
    if soma_dos_digitos == num:
        print(num)
