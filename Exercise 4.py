notas = ["", "", "", "", ""]
soma = 0
cont = 0
for a in range(len(notas)):
    notas[a] = float(input("Digite as notas: "))
for b in range(len(notas)):
    soma = soma + notas[b]
media = soma/len(notas)
for c in range(len(notas)):
    if notas[c] > media:
        cont+=1
print("")
print(f"a média geral da sala é {media:.2f} e apenas {cont} ficaram acima da média")