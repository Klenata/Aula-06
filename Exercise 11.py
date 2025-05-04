nomes = [""]*5

for i in range(len(nomes)):
    nomes[i] = input("Digite um nome: ")

print("")

print(nomes)

print("")

for y in range(len(nomes) -1, -1, -1):
    print(nomes[y])