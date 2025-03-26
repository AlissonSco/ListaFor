nn = int(input("Digite um número: "))
primo = 1

for i in range(2, nn):
    if nn % i == 0:
        primo = 0
        break

if primo == 1 and nn > 1:
    print(f"{nn} é primo.")
else:
    print(f"{nn} não é primo.")
