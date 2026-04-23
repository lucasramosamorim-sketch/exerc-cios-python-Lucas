# ex16 - Condição com AND

idade = int(input("Digite sua idade: "))
carteira = input("Tem carteira? (sim/não):")

if idade >= 18 and carteira == "sim":
    print("Pode dirigir")
else:
    print("Não pode dirigir")