'''
Fazer um programa que pergunte uma temperatura ao usuário, em graus Fahrenheit, e apresente esta
temperatura convertida em graus Celsius. A fórmula da conversão é c	=	(f	–	32)	x	5	:	9	, onde c	 é a temperatura
em graus Celsius e f		em Fahrenheit
'''

temp = float(input("Qual a temperatura a ser inserido (Fahrenheit)?"))
cel = (temp-32)*5/9
print("O valor da temperatura em graus celsius é", cel)