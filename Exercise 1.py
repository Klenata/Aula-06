nomes = ["", "", "", "", ""]
for i in range(len(nomes)):
    nomes[i] = input(f"Digite o {i+1}° nome: ")

pesquisa = input("Digite o nome que você quer pesquisar: ")
for x in range(len(nomes)):
    if pesquisa == nomes[x]:
        print(f"Está na lista, posição {x}")
        break
    else:
        print("não", end=" ")