nome = input("Digite o seu primeiro nome")
idade = input("Digite sua idade")

#print("olá", nome, "!")
#print("Tudo bem com voce?")
#print("Caranba", nome, "! voce tem", idade, "anos? Nem parece!")

print("Olá, {}!".format(nome))
print("Tudo bem com você?")

print("Caramba {}! Você tem {} anos? Nem parece.".format(nome, idade))
print(f"Caramba {nome}! Voce tem {idade} anos? Nem parece") #usar esse, melhor e mais facil
print("Caranba", nome, "! voce tem", idade, "anos? Nem parece!")