nomes = ["", "", "", "", ""]
for i in range(len(nomes)):
    nomes[i] = input(f"Digite o {i+1}° nome: ")

pesquisa = input("Digite o nome que você quer pesquisar: ")
encontrou = False  # Variável para saber se achou pelo menos uma vez

for x in range(len(nomes)):
    if pesquisa == nomes[x]:
        print(f"'{pesquisa}' está na lista, na posição {x}")
        encontrou = True

if not encontrou: #tinha colocado "if encontrou == False" mas o pycharm corrigiu...
    print(f"'{pesquisa}' não está na lista.")
