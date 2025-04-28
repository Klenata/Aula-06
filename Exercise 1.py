nomes = ["", "", "", "", ""]
for i in range(len(nomes)):
    nomes[i] = input(f"Digite o {i+1}° nome: ")

for x in range(len(nomes)):
    print(f"{x} {nomes[x]}")