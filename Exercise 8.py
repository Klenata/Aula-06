usuario = ["", "", "", "", ""]
senha = ["", "", "", "", ""]

for i in range(len(usuario)):
    usuario[i] = input("Crie seu nome de usuário:\n")
    senha[i] = input(f"Crie uma senha para o seu usuário {usuario[i]}:\n")

login = input("Digite a senha para efetuar o login: ")
for i in range(len(usuario)):
    if login == senha[i]:
        print(f"Seja Bem Vindo(a) {usuario[i]}")