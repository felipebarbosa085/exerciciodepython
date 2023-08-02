'''
Fazer um algoritmo que efetue o cálculo do valor de uma prestação em atraso, utilizando a fórmula prestação	=
valor	+	(valor	x	(taxa	:	100)	x	tempo	em	dias)
'''
val = int(input("Qual o valor da prestação?"))
tax = float(input("Qual o valor da taxa?"))
temp = int(input("Qual o tempo em atraso (dias) ?"))

prest = val +(val*(tax/100)*temp)

print("O valor da sua Prestação é de R$", prest)