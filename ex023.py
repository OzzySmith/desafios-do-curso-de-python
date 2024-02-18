#Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados
#Exemplo: 1984
#unidade:4
#dezena:8
#centena:9
#milhar:1
num = int(input('Digite um número de 0000 a 9999: '))
U = num // 1 % 10
D = num // 10 % 10
C = num // 100 % 10
M = num // 1000 % 10
print('Unidade: {}.'.format(U))
print('Dezena: {}.'.format(D))
print('Centena: {}.'.format(C))
print('Milhar: {}.'.format(M))