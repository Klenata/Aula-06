lista = [""]*10
cont = 0

for i in range(len(lista)):
    lista[i] = int(input(f"Digite o {i+1}º número: "))

busca = int(input("Digite qual número você quer buscar: "))

for i in range(len(lista)):
    if busca == lista[i]:
        cont += 1

print("")
print(f"O número {busca} aparece {cont} vezes na lista!")