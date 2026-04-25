#ex17 - Login Simples
usuario = input("Usuário: ")
senha = input("Sistema: ")

if usuario == "admin" and senha == "123":
    print("Login realizado")
else:
    print("Usuario ou senha incorretos")