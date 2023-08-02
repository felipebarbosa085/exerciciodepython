'''
Fazer um programa que calcule e apresente a quantidade de litros que um automóvel gastará em uma viagem. O
programa deve coletar as seguintes informações: Distância a percorrer na viagem, em quilômetros; qual é o
valor do consumo médio do automóvel, em quilômetros por litro
'''
dis = float(input("Qual a distancia ser percorrida?(em Km)"))
val = float(input("Quantos litros o seu automóvel consome por km?"))

per = dis/val
print("Você vai prescisar de cerca de",per,"litros")
