'''
Fazer um algoritmo que pergunte 1 número e apresente
a) O próprio número
b) O quadrado deste número
c) A raiz quadrada deste número
'''
import math

nume = int(input("Qual o numero a ser inserido?"))
print("O seu numero é", nume)

print("O quadrado desse numero é", math.pow(nume,2))

print("A raiz quadrada do seu numero é",math.sqrt(nume))