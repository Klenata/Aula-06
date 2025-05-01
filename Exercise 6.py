numeros = ["", "", "", "", ""]
for i in range(len(numeros)):
    numeros[i] = int(input("Digite um número: "))

for i in range(len(numeros)-1,-1,-1):
    print(numeros[i],end=" ")