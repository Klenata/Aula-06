usuario = ["", "", "", "", ""]
senha = ["", "", "", "", ""]

for i in range(len(usuario)):
    usuario[i] = input("Crie seu nome de usuário:\n")
    senha[i] = input("Crie uma senha para o seu usuário usuario:\n")

for i in range(len(usuario)):
    print(f"{i}. usuário: {usuario[i]}, senha: {senha[i]}")