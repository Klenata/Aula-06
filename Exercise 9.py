tamanho = int(input("Digite o tamanho que as listas terão: "))
listA = [""] * tamanho
listB = [""] * tamanho
soma = [""] * tamanho

for i in range(tamanho):
    listA[i] = int(input("Digite um número para somar: "))
    listB[i] = int(input("Digite um outro número para somar: "))
    soma[i] = listA[i] + listB[i]

print("Resultado das somas:")
for i in range(tamanho):
    print(f"{listA[i]} + {listB[i]} = {soma[i]}")