#Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.
P = float(input('Digite o valor de um produto: '))
D = P - ( P * 5 / 100)
print('O valor original do produto, de R${}, com o desconto de 5%, fica R${}.'.format(P, D))
