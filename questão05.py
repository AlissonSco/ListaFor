nn = int(input("Digite um número: "))

for i in range(2, nn):
    if nn % i == 0:
        print(f"{nn} não é primo.")
        break
else:
    print(f"{nn} é primo.")